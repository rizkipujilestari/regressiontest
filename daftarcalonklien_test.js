import http from 'k6/http';
import { check, group, sleep, fail } from 'k6';


const BASE_URL = 'http://127.0.0.1:8080';
// const BASE_URL = 'https://kumbang.torche.id:32320';


let times; 
function toSecond(times) {
  const seconds = times / 1000;
  return seconds;
}

export default function () 
{
  let requestConfig = {
    headers: {
      Authorization: "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJzWTczVmh0d2RvWG1ZdVRWRktlV0FMYXROWFkzajdoaGMzaHNqR24tRmJZIn0.eyJleHAiOjE2NzM0NDE5NTcsImlhdCI6MTY3MzQwNTk1OCwiYXV0aF90aW1lIjoxNjczNDA1OTU3LCJqdGkiOiI5MTA2NGEyMi00ZDA4LTQxMjYtODYwNy1jZjJiZDdmNzczZTgiLCJpc3MiOiJodHRwOi8vdGlnZXIudG9yY2hlLmlkOjgwMTAvYXV0aC9yZWFsbXMvZXhhbXBsZSIsInN1YiI6ImY6MjVkYWMzYTEtOTljNy00MTBlLTlmNDktNTVmOTE2ZmIzOTI2OmJhcGFzX2JhbmR1bmciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJmcm9udGVuZC1zZHAiLCJub25jZSI6ImQ2NGJlMzI4LThmOTktNDFiOS1iNjAyLWVlNTllNGNjYjJlNiIsInNlc3Npb25fc3RhdGUiOiI2OThhZTMxNS0wZDU5LTQwMzUtODZmNC02MmM0ODA3ZmJkZTYiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6MzI0MDAiLCIqIiwiaHR0cDovL2xvY2FsaG9zdDozMDAwIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiZnJvbnRlbmQtc2RwIjp7InJvbGVzIjpbImFjY2Vzc192aWV3Il19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6IjY5OGFlMzE1LTBkNTktNDAzNS04NmY0LTYyYzQ4MDdmYmRlNiIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwidXB0X3R5cGVfbmFtZSI6IkJhbGFpIFBlbWFzeWFyYWthdGFuIiwidXB0X2lkIjoiNzA3IiwibGV2ZWxfaWQiOiIyMTIiLCJwZXJtaXNzaW9uIjpbImFjY2Vzc192aWV3Il0sInByZWZlcnJlZF91c2VybmFtZSI6ImJhcGFzX2JhbmR1bmciLCJ0eXBlIjoidXB0Iiwia2Fud2lsX25hbWUiOiJKYXdhIEJhcmF0IiwidXB0X25hbWUiOiJCQVBBUyBCQU5EVU5HIiwibGV2ZWxfbmFtZSI6IlVBVCIsInVzZXJfaWQiOiIxNjEiLCJ1cHRfdHlwZV9pZCI6IkpVMTAiLCJrYW53aWxfaWQiOiIxMiIsImFjdGl2ZV9sZXZlbCI6IjIxMiIsImVtYWlsIjoiMTIzMTIzQGdtYWlsLmNvbSJ9.Jp12rUrz_0thkOdD4G1wFtrQE8B0Qwa_u85-10eEUJNZu9IjSd3elR1OPHWYe259wt0O1-nvL6idQxl7AlVNe_vjkEjvqqg2r1IUWwbyDCdeX5H16DxDMQEsDg54xHRU-jTeyUOglZRulF1erBHuYTWPOrLXx50wtefnNB08sN2mscFjv98_4YPR0xtCR1zJY-LqVWDQPzvPsnv0lRCb2rJnOK1vFj02Wg0tU1r9M2s1XlI3-OEpyymm6mRSirfD3fLjvgSpRnOxVVceVQuf4oKuVc5GqkcffpLqkwv8Zjksd1SRzG8FhnnEn4fpjcQ88qYTDeZX24xwhacZtabNpg",
    },
  };

  // const URL = `${BASE_URL}/daftar-calon-klien`;
  // const payload = { page: '1', per_page: "10" };
  // const response = http.get(URL, requestConfig);

  const payload_create = {
    nama_lengkap: `Gabriel`,
    tempat_lahir: 'Jakarta',
    tanggal_lahir: '2001-01-01',
  };

  const payload_update = {
    nama_lengkap: `Mikhael`,
    tempat_lahir: 'Jakarta',
    tanggal_lahir: '2001-01-01',
  };

  const responses = http.batch([
    ['GET', `${BASE_URL}/daftar-calon-klien`, null, requestConfig],
    ['GET', `${BASE_URL}/daftar-calon-klien/export-excel`, null, requestConfig],
    ['GET', `${BASE_URL}/daftar-calon-klien/export-pdf`, null, requestConfig],
    ['POST', `${BASE_URL}/daftar-calon-klien`, payload_create, requestConfig],
    ['PUT', `${BASE_URL}/daftar-calon-klien/70720230110001`, payload_update, requestConfig],
    ['GET', `${BASE_URL}/daftar-calon-klien/dropdown`, null, requestConfig],
  ]);

  
  let response_code = Object.values(responses).map((res) => res.status);
  let content = Object.values(responses).map((res) => res.body);
  let execute_time = Object.values(responses).map((res) => res.timings.duration);

  // console.log(response_code);
  
  for (let no = 0; no < response_code.length; no++) {
    const rc = response_code[no];
    times    = execute_time[no];

    console.log("RC: " + rc + " - Time: " + times + " ms");
  }


  sleep(1);
}