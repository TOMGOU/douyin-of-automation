from translate import Translator
import os 

# translator= Translator(from_lang="chinese",to_lang="english")
# translator= Translator(from_lang="english",to_lang="chinese")
# translator= Translator(from_lang="english",to_lang="japanese")
# translator= Translator(from_lang="english",to_lang="korean")
# translator= Translator(from_lang="english",to_lang="french")
# translator= Translator(from_lang="english",to_lang="russian")
translator= Translator(from_lang="chinese",to_lang="spanish")

def rename_file(file_dir):   
  L = [] 
  index = 1
  for root, dirs, files in os.walk(file_dir):
    length = len(files)
    for file in files: 
      if os.path.splitext(file)[1] == '.mp4': 
        print('当前翻译进度：', str(index) +'/' + str(length))
        index = index + 1
        name_original = os.path.splitext(file)[0]
        name_translated = translator.translate(os.path.splitext(file)[0]).rstrip()
        postfix = os.path.splitext(file)[1]
        os.rename(os.path.join(root, name_original + postfix), os.path.join(root, name_translated + postfix))
        L.append(name_translated + postfix)
  # print(L)
  print('翻译总览：' + str(index - 1) + '个文件已翻译完成，其中' + str(length - index + 1) + '个文件为非MP4文件',) 
  return L

rename_file(r'/Users/tangyong/test/douyin/videos')