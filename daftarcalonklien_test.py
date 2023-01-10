import requests
import json
# from postpy2.core import PostPython
from postman2py.core import PostPython
from humanfriendly import format_timespan
import time



begin_time = time.time()

local  = "http://localhost:8080/"
server = "http://kumbang.torche.id:32320"

headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJzWTczVmh0d2RvWG1ZdVRWRktlV0FMYXROWFkzajdoaGMzaHNqR24tRmJZIn0.eyJleHAiOjE2NzMzNjIzNzgsImlhdCI6MTY3MzMyNjM3OSwiYXV0aF90aW1lIjoxNjczMzI2Mzc4LCJqdGkiOiJlZDUxNDc2Mi01M2VjLTQ5MGMtOGVlNy02NmM5ZjE0MDAzNDciLCJpc3MiOiJodHRwOi8vdGlnZXIudG9yY2hlLmlkOjgwMTAvYXV0aC9yZWFsbXMvZXhhbXBsZSIsInN1YiI6ImY6MjVkYWMzYTEtOTljNy00MTBlLTlmNDktNTVmOTE2ZmIzOTI2OmJhcGFzX2JhbmR1bmciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJmcm9udGVuZC1zZHAiLCJub25jZSI6IjQzNTMwODEyLWE2OTktNDdjOC05Mzk0LWIwNThhMGE0NzQyNSIsInNlc3Npb25fc3RhdGUiOiI2MjM1M2YzOS0zNzEyLTRhYTEtYTdiMC1hZmFiMmMxZGE5YzgiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzI0MDAiLCIqIiwiaHR0cDovL2xvY2FsaG9zdDozMDAwIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiZnJvbnRlbmQtc2RwIjp7InJvbGVzIjpbImFjY2Vzc192aWV3Il19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6IjYyMzUzZjM5LTM3MTItNGFhMS1hN2IwLWFmYWIyYzFkYTljOCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwidXB0X3R5cGVfbmFtZSI6IkJhbGFpIFBlbWFzeWFyYWthdGFuIiwidXB0X2lkIjoiNzA3IiwibGV2ZWxfaWQiOiIyMTIiLCJwZXJtaXNzaW9uIjpbImFjY2Vzc192aWV3Il0sInByZWZlcnJlZF91c2VybmFtZSI6ImJhcGFzX2JhbmR1bmciLCJ0eXBlIjoidXB0Iiwia2Fud2lsX25hbWUiOiJKYXdhIEJhcmF0IiwidXB0X25hbWUiOiJCQVBBUyBCQU5EVU5HIiwibGV2ZWxfbmFtZSI6IlVBVCIsInVzZXJfaWQiOiIxNjEiLCJ1cHRfdHlwZV9pZCI6IkpVMTAiLCJrYW53aWxfaWQiOiIxMiIsImFjdGl2ZV9sZXZlbCI6IjIxMiIsImVtYWlsIjoiMTIzMTIzQGdtYWlsLmNvbSJ9.Vsfa5UlW2ssli64DMvpOLEx-17OdegvHbX77rntSZojfOuuj9SiJUT6tKabaUNw_h7DRKIOsaW-z7l3vvkGYk_EYlPV1aJo6W7ycEWpZQxmggow1YeC9oaw5JKn9FARaAFg3IPKp7Ix0HOD4nvAQj4eoNR0DJ2PtVjgY2uNs2hFiQl5Y2_lHg1zrho5bsQwmNqkJfFfRpNTflpNRMDH4mjOuNRKz5_XGQucQ_z6TDwLtwY44LjnBA3p6VJhWcVFUjvmxAnl3VuffV08_-bsgECD-ER5Mlql-XucZE6BPkPziYoIwsUgOxiad9_cGfWHnARHNlIHkCwMYsd0SQpO81A"}

runner = PostPython('collections/bapas-pendaftaran_ver1.postman_collection.json')
# runner = PostPython('collections/bapas-pendaftaran_ver1.postman_collection.json', request_overrides={
#     'headers': headers
# })

main_grid          = runner.DaftarCalonKlien.daftar_calon_klien_main_grid()
service_main_grid  = local + "daftar-calon-klien"
res_main_grid      = requests.get(service_main_grid, headers=headers, data=main_grid) 
end_time_main_grid = time.time() - begin_time
exetime_main_grid  = "Execution Time: " + format_timespan(end_time_main_grid) 

# print(res_main_grid.status_code)
# print(exetime_main_grid)
# print(res_main_grid.json())

dropdown          = runner.DaftarCalonKlien.daftar_calon_klien_dropdown()
service_dropdown  = local + "daftar-calon-klien/dropdown"
res_dropdown      = requests.get(service_dropdown, headers=headers, data=dropdown)
end_time_dropdown = time.time() - begin_time
exetime_dropdown  = "Execution Time: " + format_timespan(end_time_dropdown)

export_pdf          = runner.DaftarCalonKlien.daftar_calon_klien_export_pdf()
service_export_pdf  = local + "daftar-calon-klien/export-pdf"
res_export_pdf      = requests.get(service_export_pdf, headers=headers, data=export_pdf)
end_time_export_pdf = time.time() - begin_time
exetime_export_pdf  = "Execution Time: " + format_timespan(end_time_export_pdf)

export_excel          = runner.DaftarCalonKlien.daftar_calon_klien_export_excel()
service_export_excel  = local + "daftar-calon-klien/export-excel"
res_export_excel      = requests.get(service_export_excel, headers=headers, data=export_excel)
end_time_export_excel = time.time() - begin_time
exetime_export_excel  = "Execution Time: " + format_timespan(end_time_export_excel)

create          = runner.DaftarCalonKlien.daftar_calon_klien_create()
service_create  = local + "daftar-calon-klien"
res_create      = requests.post(service_create, headers=headers, data=create)
end_time_create = time.time() - begin_time
exetime_create  = "Execution Time: " + format_timespan(end_time_create)

show          = runner.DaftarCalonKlien.daftar_calon_klien_id_show()
service_show  = local + "daftar-calon-klien/50120221228002"
res_show      = requests.get(service_show, headers=headers, data=show)
end_time_show = time.time() - begin_time
exetime_show  = "Execution Time: " + format_timespan(end_time_show)

hasil = [
    [service_main_grid, res_main_grid.status_code, res_main_grid.json(), exetime_main_grid],
    [service_dropdown, res_dropdown.status_code, res_dropdown.json(), exetime_dropdown],
    [service_export_pdf, res_export_pdf.status_code, res_export_pdf, exetime_export_pdf],
    [service_export_excel, res_export_excel.status_code, res_export_excel, exetime_export_excel],
    [service_create, res_create.status_code, res_create.json(), exetime_create],
    [service_show, res_show.status_code, res_show.json(), exetime_show],
]
# print(hasil)

print(res_create.json())

# from bs4 import BeautifulSoup
# import re

# url='http://www.xetra.com/xetra-en/instruments/etf-exchange-traded-funds/list-of-tradable-etfs'
# html=requests.get(url)
# page=BeautifulSoup(html.content, features="lxml")
# reg=re.compile('Master data')
# find=page.find('span',text=reg)  #find the file url
# file_url='http://www.xetra.com'+find.parent['href']
# file=requests.get(file_url)
# with open(r'C:\\Users\user\Downloads\export_excel.xlsx','wb') as ff:
#     ff.write(file.content)