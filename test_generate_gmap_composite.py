import xmlrpclib
import sys

if __name__=="__main__":
  import os
  PATHNAME=os.path.dirname(os.path.abspath(sys.argv[0]))

  FIXTURES1=[PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_seang_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_searl_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_sease_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_sehud_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_sekir_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_sekkr_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_selek_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_selul_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_seosu_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_seovi_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_sevar_000000.h5",
             PATHNAME +"/fixtures/Z_SCAN_C_ESWI_20101016080000_sevil_000000.h5"]

  server = xmlrpclib.ServerProxy("http://localhost:8085/RAVE")

  arguments = ["--area=swegmaps_2000", "--date=20101016", "--time=080000", "--method=pcappi", "--height=1000", "--quantity=DBZH"]

  server.generate("eu.baltrad.beast.generatecomposite", FIXTURES1, arguments)


