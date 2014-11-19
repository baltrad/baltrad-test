import _raveio
import _ravefield
import numpy
import datetime
import BaltradFrame

if __name__=="__main__":
  n = datetime.datetime.now()
  hourback = 12
  rio = _raveio.open("cartesian_image.h5")
  o = rio.object
  qf = _ravefield.new()
  qf.setData(numpy.zeros((o.xsize,o.ysize), numpy.uint8))
  qf.addAttribute("how/task", "se.smhi.composite.distance.radar")
  qf.addAttribute("what/nodata", -1.0)
  qf.addAttribute("what/undetect", 0.0)
  o.getParameter("DBZH").addQualityField(qf)

  d = n - datetime.timedelta(0,3600 * (hourback-1))
  for x in range(hourback):
    datestr="%d%02d%02d"%(d.year, d.month,d.day)
    timestr="%02d%02d%02d"%(d.hour, 0, 0)
    print datestr + timestr
    d = d + datetime.timedelta(0,3600)
    o.startdate = datestr
    o.date = datestr
    o.starttime = timestr
    o.time = timestr
    o.source = "ORG:82,CMT:testgmaps_2000"
    nrio = _raveio.new()
    nrio.object = o
    try:
      nrio.save("/tmp/acrr_file_%s%s.h5"%(o.date,o.time))
      print "INJECTING FILE /tmp/acrr_file_%s%s.h5"%(o.date,o.time)
      #BaltradFrame.inject_file("/tmp/acrr_file_%s%s.h5"%(o.date,o.time), "http://localhost:8080/BaltradDex")
    except Exception, e:
      print e.__str__()
    finally:
      pass
      #try:
      #  os.unlink("/tmp/acrr_file_%s%s.h5"%(o.date,o.time))
      #except:
      #  pass
a="""
  rio = _raveio.open("cartesian_image.h5")

  dates = [
    ("20100101", "100000"),
    ("20100101", "101500"),
    ("20100101", "103000"),
    ("20100101", "104500"),
    ("20100101", "110000"),
    ("20100101", "111500"),
    ("20100101", "113000"),
    ("20100101", "114500"),
    ("20100101", "120000"),
    ("20100101", "121500")]

  o = rio.object
  qf = _ravefield.new()
  qf.setData(numpy.zeros((o.xsize,o.ysize), numpy.uint8))
  qf.addAttribute("how/task", "se.smhi.composite.distance.radar")
  qf.addAttribute("what/nodata", -1.0)
  qf.addAttribute("what/undetect", 0.0)
  o.getParameter("DBZH").addQualityField(qf)

  for d in dates:
    o.startdate = d[0]
    o.date = d[0]
    o.starttime = d[1]
    o.time = d[1]
    o.source = "ORG:82,CMT:testgmaps_2000"
    nrio = _raveio.new()
    nrio.object = o
    nrio.save("acrr_fixture_wqf_%s%s.h5"%(o.date,o.time))

  o.startdate = dates[4][0]
  o.date = dates[4][0]
  o.starttime = dates[4][1]
  o.time = dates[4][1]
  o.source = "ORG:82,CMT:testgmaps_2000"
  o.getParameter("DBZH").gain = 1.1
  nrio = _raveio.new()
  nrio.object = o
  nrio.save("acrr_fixture_wqf_%s%s_dup.h5"%(o.date,o.time))
"""

    

