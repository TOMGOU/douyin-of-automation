import os 
from translate import Translator

translator= Translator(to_lang="chinese")

def file_name(file_dir):   
    L={'file_name': [], 'url_name': []}  
    for root, dirs, files in os.walk(file_dir):  
      # print('文件名：', files)
      for file in files:  
        if os.path.splitext(file)[1] == '.mp4':  
          L['url_name'].append(os.path.join(root, file))
          name_of_video = translator.translate(os.path.splitext(file)[0])
          L['file_name'].append(name_of_video)
    print('文件名：', L['file_name'])              
    return L
  
# def file_name(file_dir):   
#     L={'file_name': [], 'url_name': []}  
#     for root, dirs, files in os.walk(file_dir):  
#       # print('文件名：', files)
#       for file in files:  
#         if os.path.splitext(file)[1] == '.mp4':  
#           L['file_name'].append(os.path.join(root, file))
#           L['url_name'].append(os.path.splitext(file)[0])
#     print('文件名：', L)              
#     return L  
file_name(r'C:\Users\zhuan\Downloads')
