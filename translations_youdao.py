import requests

string = "Las 20 ciudades más pobladas del mundo de 1500 a 2100 (Historia y Proyección)"
data = {
'doctype': 'json',
'type': 'SP2ZH_CN',
'i': string
}
url = "http://fanyi.youdao.com/translate"
for index in range(2):
  r = requests.get(url,params=data)
  result = r.json()
  print(index, ':', result['translateResult'][0][0]['tgt'])