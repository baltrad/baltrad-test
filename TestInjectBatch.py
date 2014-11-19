import _raveio
import _ravefield, _polarvolume
import numpy
import BaltradFrame
import sys, time, datetime, getopt, string, re, os
import rave_tempfile

FIXTURES_SCAN=["fixtures/Z_SCAN_C_ESWI_20101016080000_seang_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_searl_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_sease_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_sehud_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_sekir_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_sekkr_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_selek_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_selul_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_seosu_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_seovi_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_sevar_000000.h5",
	       "fixtures/Z_SCAN_C_ESWI_20101016080000_sevil_000000.h5"]

FIXTURES_PVOL=["fixtures4/seang_pvol_20140220T1300Z.h5",
               "fixtures4/searl_pvol_20140220T1300Z.h5",
               "fixtures4/sease_pvol_20140220T1300Z.h5",
               "fixtures4/sehud_pvol_20140220T1300Z.h5",
               "fixtures4/sekir_pvol_20140220T1300Z.h5",
               "fixtures4/sekkr_pvol_20140220T1300Z.h5",
               "fixtures4/selek_pvol_20140220T1300Z.h5",
               "fixtures4/selul_pvol_20140220T1300Z.h5",
               "fixtures4/seosu_pvol_20140220T1300Z.h5",
               "fixtures4/seovi_pvol_20140220T1300Z.h5",
               "fixtures4/sevar_pvol_20140220T1300Z.h5",
               "fixtures4/sevil_pvol_20140220T1300Z.h5"]


class filebatch(object):
  def __init__(self, dtstr=None, interval=15, periods=1, reruns=0, sources=[], ftype="SCAN"):
    self.dtstr = dtstr
    if dtstr is None:
      self.dt = self.get_closest_time(interval)
    else:
      self.dt = self.parse_datetime_str(dtstr, interval)
    self.interval = interval
    self.periods = periods
    self.reruns = reruns
    self.sources = sources
    self.ftype = ftype
    self.addmalfunc = False

  def __str__(self):
    return "%s: interval = %d, periods = %d, reruns = %d"%(self.dt.strftime("%Y%m%d%H%M%S"),self.interval,self.periods, self.reruns)

  def __repr__(self):
    return self.__str__()

  def execute_once(self):
    for pindex in range(self.periods):
      tstr = (self.dt + datetime.timedelta(minutes = pindex*self.interval)).strftime("%Y%m%d%H%M%S")
      print "Injecting files for %s"%tstr
      d = tstr[:8]
      t = tstr[8:]
      avgtime = 0.0
      fixtures = FIXTURES_SCAN
      if self.ftype == "PVOL":
        fixtures = FIXTURES_PVOL

      nrfiles=0
      for f in fixtures:
        obj = _raveio.open(f).object
        obj.date = d
        obj.time = t

        if self.addmalfunc:
          obj.addAttribute("how/malfunc", 'True')

        if _polarvolume.isPolarVolume(obj):
          for i in range(obj.getNumberOfScans()):
            scan = obj.getScan(i)
            scan.date = d
            scan.time = t

        if len(self.sources) > 0:
          if self.ftype == "SCAN":
            srcm = f[38:43]
          else:
            srcm = f[10:15]
          if not srcm in self.sources:
            continue

        o = _raveio.new()
        o.object = obj
        fileno, outfile = rave_tempfile.mktemp(suffix='.h5', close="True")
        currt = time.clock()
        try:
          o.save(outfile)
          BaltradFrame.inject_file(outfile, "http://localhost:8080/BaltradDex")
          injet = time.clock() - currt
          avgtime = avgtime + injet
          nrfiles = nrfiles + 1
        finally:
          try:
            os.unlink(outfile)
          except:
            pass
      if nrfiles != 0:
        print "File injection of %d files took an average of %f seconds"%(nrfiles, (avgtime / nrfiles))

  def get_closest_time(self, interval):
    t = time.localtime()
    oz = t.tm_min%interval
    return datetime.datetime(t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min-oz,0)

  def parse_datetime_str(self, dtstr, interval):
    year = int(dtstr[:4])
    month = int(dtstr[4:6])
    mday = int(dtstr[6:8])
    hour = int(dtstr[8:10])
    minute = int(dtstr[10:12])
    minute = minute - minute%interval
    return datetime.datetime(year,month,mday,hour,minute,0)

if __name__=="__main__":
  dstr = None
  interval = 15
  periods = 1
  reruns = 0
  sources = []
  ftype = "SCAN"
  addmalfunc = False

  optlist = []
  args = []
  try:
    optlist, args = getopt.getopt(sys.argv[1:], '', 
                                  ['datetime=','interval=','periods=','reruns=','sources=','type=', 'addmalfunc'])
  except getopt.GetoptError, e:
    print e.__str__()
    sys.exit(127)

  for o, a in optlist:
    if o == "--datetime":
      dstr = a
    elif o == "--interval":
      interval = int(a)
    elif o == "--periods":
      periods = int(a)
    elif o == "--reruns":
      reruns = int(a)
    elif o == "--sources":
      sources = string.split(a,',')
    elif o == "--type":
      if a in ["PVOL", "SCAN"]:
        ftype = a
      else:
        print "Ignoring type since it isn't PVOL or SCAN"
    elif o == "--addmalfunc":
      addmalfunc = True
  a = filebatch(dstr, interval, periods, reruns, sources, ftype)
  a.addmalfunc = addmalfunc
  a.execute_once()

