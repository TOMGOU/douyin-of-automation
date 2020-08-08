# 自动检测	auto	中文	zh	英语	en
# 粤语	yue	文言文	wyw	日语	jp
# 韩语	kor	法语	fra	西班牙语	spa
# 泰语	th	阿拉伯语	ara	俄语	ru
# 葡萄牙语	pt	德语	de	意大利语	it
# 希腊语	el	荷兰语	nl	波兰语	pl
# 保加利亚语	bul	爱沙尼亚语	est	丹麦语	dan
# 芬兰语	fin	捷克语	cs	罗马尼亚语	rom
# 斯洛文尼亚语	slo	瑞典语	swe	匈牙利语	hu
# 繁体中文	cht	越南语	vie	 	
# 
# QPS = 10 (每秒10次访问量)

import requests
import time
import hashlib

q = "ciudades más"
key = "C4_azdaSXSfteFdUHZey"
appid = '20200808000537597'
salt = str(time.time())
sign = appid + q + salt + key
m = hashlib.new("md5")  
m.update(sign.encode(encoding="utf-8"))  # 注意使用utf-8编码
msign = m.hexdigest() # 得到原始签名的MD5值
data = {
'q': q,
'from': 'spa',
'to': 'zh',
'appid': appid,
'salt': salt,
'sign': msign
}
url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
for index in range(2):
  r = requests.get(url, params = data)
  result = r.json()
  print(index, ':', result)
  print(index, ':', result['trans_result'][0]['dst'])