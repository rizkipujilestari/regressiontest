import requests
import json
import timeit
from tomlkit import item
from postpy2.core import PostPython
# from postman2py.core import PostPython  # 401 no auth
from datetime import datetime
from humanfriendly import format_timespan
import time


begin_time = time.time()

# ----- 401 no auth ------
# runner = PostPython('collection/bapas-pendaftaran_ver1.postman_collection.json')
# runner.environments.load('environtment/bapas.postman_env.json')


# harus check expired token
headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJzWTczVmh0d2RvWG1ZdVRWRktlV0FMYXROWFkzajdoaGMzaHNqR24tRmJZIn0.eyJleHAiOjE2NzI5MjI5NzgsImlhdCI6MTY3Mjg4Njk3OSwiYXV0aF90aW1lIjoxNjcyODg2OTc4LCJqdGkiOiIyMTMyYWMxYy0wODZhLTQ0ZWQtOTI2Zi04NDI2NWI4OTAwNGIiLCJpc3MiOiJodHRwOi8vdGlnZXIudG9yY2hlLmlkOjgwMTAvYXV0aC9yZWFsbXMvZXhhbXBsZSIsInN1YiI6ImY6MjVkYWMzYTEtOTljNy00MTBlLTlmNDktNTVmOTE2ZmIzOTI2OmJhcGFzX2JhbmR1bmciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJmcm9udGVuZC1zZHAiLCJub25jZSI6IjVkMWRhNDAwLTllYjEtNGMxOS04ZmQzLWM0YWRjMmI4NTE0YiIsInNlc3Npb25fc3RhdGUiOiJkNzY1YjdmMy0yOTgwLTQyM2YtYjY0MC01ZmUxZjA2MzdiOTMiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzI0MDAiLCIqIiwiaHR0cDovL2xvY2FsaG9zdDozMDAwIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiZnJvbnRlbmQtc2RwIjp7InJvbGVzIjpbImFjY2Vzc192aWV3Il19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6ImQ3NjViN2YzLTI5ODAtNDIzZi1iNjQwLTVmZTFmMDYzN2I5MyIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwidXB0X3R5cGVfbmFtZSI6IkJhbGFpIFBlbWFzeWFyYWthdGFuIiwidXB0X2lkIjoiNzA3IiwibGV2ZWxfaWQiOiIyMTIiLCJwZXJtaXNzaW9uIjpbImFjY2Vzc192aWV3Il0sInByZWZlcnJlZF91c2VybmFtZSI6ImJhcGFzX2JhbmR1bmciLCJ0eXBlIjoidXB0Iiwia2Fud2lsX25hbWUiOiJKYXdhIEJhcmF0IiwidXB0X25hbWUiOiJCQVBBUyBCQU5EVU5HIiwibGV2ZWxfbmFtZSI6IlVBVCIsInVzZXJfaWQiOiIxNjEiLCJ1cHRfdHlwZV9pZCI6IkpVMTAiLCJrYW53aWxfaWQiOiIxMiIsImFjdGl2ZV9sZXZlbCI6IjIxMiIsImVtYWlsIjoiMTIzMTIzQGdtYWlsLmNvbSJ9.KB3C3hG9LyTTiPX6lsTadRWDzj3Zbh7TMEc_XK-AvsRMbCKmH4xUoOooz0k7E3ZBMQx8IPO6SVtR-fMnA1sz1NN_i4elEl47d6gpuqxQuVd7tmgilrvU2cfxxg4ZL_c3ZDKxuQjsWWWIj5-WVDZBg14VbCzFDzbfWR94iJnmiUYUs8Zdq7IIuw31PtFoTyC81s8NGEefVOzLv3Pc8cdFr-3jIUJN51pQ7Cxq8UIjW9xxwUiZs0CJeHtCl-_e97s1SGaJaW_Gi2KMZbap4glfTAycRONdHSoFDBHMBc9KBFVwbPEs691Hm8UOlMrsMDUzkGexg6eM5af_-yDmlRfXZw"}
runner = PostPython('collections/bapas-pendaftaran_ver1.postman_collection.json', request_overrides={
    'headers': headers
})

response = runner.DaftarCalonKlien.daftar_calon_klien_export_excel()

end_time = time.time() - begin_time
exetime = "execution time: ", format_timespan(end_time)
print(exetime)
print(response.status_code)
print(response.json())


# response = []

# service             = "http://localhost:8080/"
# main_grid           = runner.DaftarCalonKlien.daftar_calon_klien_main_grid()
# status_code1        = main_grid.status_code
# end_time_main_grid  = time.time() - begin_time
# time1               = format_timespan(end_time_main_grid)

# service             = "http://localhost:8080/"
# dropdown            = runner.DaftarCalonKlien.daftar_calon_klien_dropdown()
# status_code2        = dropdown.status_code
# end_time_dropdown   = time.time() - begin_time
# time2               = format_timespan(end_time_dropdown)

# response["export_pdf"]["data"]   = runner.DaftarCalonKlien.daftar_calon_klien_export_pdf()
# response["export_pdf"]["status"] = response["export_pdf"]["data"].status_code
# end_time_export_pdf              = time.time() - begin_time
# response["export_pdf"]["time"]   = format_timespan(end_time_export_pdf)

# response["export_excel"]["data"]   = runner.DaftarCalonKlien.daftar_calon_klien_export_excel()
# response["export_excel"]["status"] = response["export_excel"]["data"].status_code
# end_time_export_excel              = time.time() - begin_time
# response["export_excel"]["time"]   = format_timespan(end_time_export_excel)

# response["create"]["data"]   = runner.DaftarCalonKlien.daftar_calon_klien_create()
# response["create"]["status"] = response["create"]["data"].status_code
# end_time_create              = time.time() - begin_time
# response["create"]["time"]   = format_timespan(end_time_create)

# response["update"]["data"]   = runner.DaftarCalonKlien.daftar_calon_klien_id_update()
# response["update"]["status"] = response["update"]["data"].status_code
# end_time_update              = time.time() - begin_time
# response["update"]["time"]   = format_timespan(end_time_update)

# response["show"]["data"]     = runner.DaftarCalonKlien.daftar_calon_klien_id_show()
# response["show"]["status"]   = response["show"]["data"].status_code
# end_time_show                = time.time() - begin_time
# response["show"]["time"]     = format_timespan(end_time_show)

# response = [
#    [main_grid, status_code1, time1],
#    [dropdown, status_code2, time2],
# ]

# print(response)
