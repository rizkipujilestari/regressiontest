import requests
import json
# from postpy2.core import PostPython
from postman2py.core import PostPython
from humanfriendly import format_timespan
import time



begin_time = time.time()

local  = "http://localhost:8080/"
server = "http://kumbang.torche.id:32320"

headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJzWTczVmh0d2RvWG1ZdVRWRktlV0FMYXROWFkzajdoaGMzaHNqR24tRmJZIn0.eyJleHAiOjE2NzM0NDE5NTcsImlhdCI6MTY3MzQwNTk1OCwiYXV0aF90aW1lIjoxNjczNDA1OTU3LCJqdGkiOiI5MTA2NGEyMi00ZDA4LTQxMjYtODYwNy1jZjJiZDdmNzczZTgiLCJpc3MiOiJodHRwOi8vdGlnZXIudG9yY2hlLmlkOjgwMTAvYXV0aC9yZWFsbXMvZXhhbXBsZSIsInN1YiI6ImY6MjVkYWMzYTEtOTljNy00MTBlLTlmNDktNTVmOTE2ZmIzOTI2OmJhcGFzX2JhbmR1bmciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJmcm9udGVuZC1zZHAiLCJub25jZSI6ImQ2NGJlMzI4LThmOTktNDFiOS1iNjAyLWVlNTllNGNjYjJlNiIsInNlc3Npb25fc3RhdGUiOiI2OThhZTMxNS0wZDU5LTQwMzUtODZmNC02MmM0ODA3ZmJkZTYiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzI0MDAiLCIqIiwiaHR0cDovL2xvY2FsaG9zdDozMDAwIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiZnJvbnRlbmQtc2RwIjp7InJvbGVzIjpbImFjY2Vzc192aWV3Il19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6IjY5OGFlMzE1LTBkNTktNDAzNS04NmY0LTYyYzQ4MDdmYmRlNiIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwidXB0X3R5cGVfbmFtZSI6IkJhbGFpIFBlbWFzeWFyYWthdGFuIiwidXB0X2lkIjoiNzA3IiwibGV2ZWxfaWQiOiIyMTIiLCJwZXJtaXNzaW9uIjpbImFjY2Vzc192aWV3Il0sInByZWZlcnJlZF91c2VybmFtZSI6ImJhcGFzX2JhbmR1bmciLCJ0eXBlIjoidXB0Iiwia2Fud2lsX25hbWUiOiJKYXdhIEJhcmF0IiwidXB0X25hbWUiOiJCQVBBUyBCQU5EVU5HIiwibGV2ZWxfbmFtZSI6IlVBVCIsInVzZXJfaWQiOiIxNjEiLCJ1cHRfdHlwZV9pZCI6IkpVMTAiLCJrYW53aWxfaWQiOiIxMiIsImFjdGl2ZV9sZXZlbCI6IjIxMiIsImVtYWlsIjoiMTIzMTIzQGdtYWlsLmNvbSJ9.Jp12rUrz_0thkOdD4G1wFtrQE8B0Qwa_u85-10eEUJNZu9IjSd3elR1OPHWYe259wt0O1-nvL6idQxl7AlVNe_vjkEjvqqg2r1IUWwbyDCdeX5H16DxDMQEsDg54xHRU-jTeyUOglZRulF1erBHuYTWPOrLXx50wtefnNB08sN2mscFjv98_4YPR0xtCR1zJY-LqVWDQPzvPsnv0lRCb2rJnOK1vFj02Wg0tU1r9M2s1XlI3-OEpyymm6mRSirfD3fLjvgSpRnOxVVceVQuf4oKuVc5GqkcffpLqkwv8Zjksd1SRzG8FhnnEn4fpjcQ88qYTDeZX24xwhacZtabNpg"}

runner = PostPython('collections/bapas-registrasi.postman_collection.json')
# runner = PostPython('collections/bapas-pendaftaran_ver1.postman_collection.json', request_overrides={
#     'headers': headers
# })

runner.environments.load('environtment\\bapas.postman_environtment.json')

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
print(hasil)

# print(res_create.json())

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