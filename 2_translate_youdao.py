# 翻译结果只支持中英互译，翻译结果支持英日韩到中文的翻译以及中文到英语的翻译
# ZH_CN2EN 中文 -> 英语 
# ZH_CN2JA 中文 -> 日语 
# ZH_CN2KR 中文 -> 韩语 
# ZH_CN2FR 中文 -> 法语 
# ZH_CN2RU 中文 -> 俄语 
# ZH_CN2SP 中文 -> 西语 
# EN2ZH_CN 英语 -> 中文 
# JA2ZH_CN 日语 -> 中文 
# KR2ZH_CN 韩语 -> 中文 
# FR2ZH_CN 法语 -> 中文 
# RU2ZH_CN 俄语 -> 中文 
# SP2ZH_CN 西语 -> 中文
# AUTO 自动
import os
import requests
import time  # 引入time模块

def trans(string):
  data = {
  'doctype': 'json',
  'type': 'SP2ZH_CN',
  'i': string
  }
  url = "http://fanyi.youdao.com/translate"
  r = requests.get(url,params=data)
  result = r.json()
  return result['translateResult'][0][0]['tgt']

def rename_file(file_dir):   
  L = [] 
  index = 1
  for root, dirs, files in os.walk(file_dir):
    length = len(files)
    for file in files: 
      if os.path.splitext(file)[1] == '.mp4' or os.path.splitext(file)[1] == '.webm': 
        print('当前翻译进度：', str(index) +'/' + str(length))
        index = index + 1
        name_original = os.path.splitext(file)[0]
        name_translated = trans(os.path.splitext(file)[0]).rstrip()

        postfix = os.path.splitext(file)[1]
        os.rename(os.path.join(root, name_original + postfix), os.path.join(root, name_translated + postfix))
        L.append(name_translated + postfix)
  # print(L)
  print('翻译总览：' + str(index - 1) + '个文件已翻译完成，其中' + str(length - index + 1) + '个文件为非视频文件',) 
  return L

start = time.time()
rename_file(r'C:\demo\02_SUMMARY\29_automation\douyin-of-automation\videos')
end = time.time()
print(end - start)