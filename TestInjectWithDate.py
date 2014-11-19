import _raveio
import _ravefield
import numpy
import BaltradFrame
import sys, time, os
import rave_tempfile
import traceback

if __name__=="__main__":
  FIXTURES1=["fixtures/Z_SCAN_C_ESWI_20101016080000_seang_000000.h5",
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

  #FIXTURES1=["fixtures/Z_SCAN_C_ESWI_20101016080000_seang_000000.h5"]

  #FIXTURES1=["fixtures3/pvol_sehud_20090501T120000Z.h5"]

  for file in FIXTURES1:
    tstr = time.strftime("%Y%m%d%H%M%S")
    if len(sys.argv) > 1:
      tstr = sys.argv[1]
      if len(tstr) != 14:
        raise Exception, "Must specify datetime as YYYYmmddHHMMSS"
    d = tstr[:8]
    t = tstr[8:]
    #print "D / T = %s%s"%(d,t)
    scan = _raveio.open(file).object
    scan.date = d
    scan.time = t
    o = _raveio.new()
    o.object = scan
    fileno, outfile = rave_tempfile.mktemp(suffix='.h5', close="True")
    currt = time.clock()
    try:
      o.save(outfile)
      BaltradFrame.inject_file(outfile, "http://localhost:8080/BaltradDex")
      injet = time.clock() - currt
      print "File injection took : %f"%injet
    finally:
      try:
        os.unlink(outfile)
      except Exception, e:
        print "Failed to unlink %s : %s"%(outfile, e.__str__())
        traceback.print_stack()

    #BaltradFrame.inject_file(file, "http://localhost:8080/BaltradDex")
