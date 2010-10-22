import BaltradFrame

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

  FIXTURES2=["fixtures/Z_SCAN_C_ESWI_20101016080500_seang_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_searl_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_sease_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_sehud_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_sekir_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_sekkr_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_selek_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_selul_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_seosu_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_seovi_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_sevar_000000.h5",
             "fixtures/Z_SCAN_C_ESWI_20101016080500_sevil_000000.h5"]

  for file in FIXTURES1:
    BaltradFrame.inject(file, channel="smhi_products", url="http://localhost:8080/BaltradDex/dispatch.htm", sender="admin")

