import requests

string = "请输入一段要翻译的文字:平时经常在网上翻译一些单词，突发奇想，可不可以直接调某些免费翻译网站的接口呢？"
data = {
'doctype': 'json',
'type': 'AUTO',
'i': string
}
url = "http://fanyi.youdao.com/translate"
# for index in range(10):
r = requests.get(url,params=data)
# result = r.json()
print(r.text)
# print(index, ':', result['translateResult'][0][0]['tgt'])