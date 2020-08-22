from selenium import webdriver
import os 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

def file_name(file_dir):   
    L={'file_name': [], 'url_name': []}  
    for root, dirs, files in os.walk(file_dir):
      for file in files:  
        if os.path.splitext(file)[1] == '.mp4':  
          L['url_name'].append(os.path.join(root, file))
          L['file_name'].append(os.path.splitext(file)[0])           
    return L

def isElementExist(browser, element):
  flag=True
  try:
    browser.find_element_by_css_selector(element)
    return flag
  
  except:
    flag=False
    return flag

option = webdriver.ChromeOptions()
option.add_argument(r'user-data-dir=C:\Users\zhuan\AppData\Local\Google\Chrome\User Data')
browser = webdriver.Chrome(chrome_options=option)
# browser = webdriver.Chrome(executable_path='/Users/tangyong/Application/chromedriver')
# browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.get('https://creator.douyin.com/content/upload')

time.sleep(5)
exiting = isElementExist(browser, 'button.semi-button-primary')
if exiting:
  button = browser.find_element_by_class_name('semi-button-primary')
  button.click()
  print('请扫码登录！')

upload_file = file_name(r'C:\demo\02_SUMMARY\29_automation\douyin-of-automation\videos') 

total_num = len(upload_file['file_name'])

index_int = 0
for index in range(total_num):
  # if index < 0:
  #   continue
  print('视频上传进度:', index + 1, '/', total_num)
  WebDriverWait(browser, 300).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(text(),"发布视频") and @class="semi-navigation-item-text"]')))
  
  time.sleep(3)
  video_upload = browser.find_element_by_xpath('//*[contains(text(),"发布视频") and @class="semi-navigation-item-text"]')
  video_upload.click()

  upload_button = browser.find_element_by_class_name('upload-btn-input--1NeEX')

  time.sleep(1)
  upload_button.send_keys(upload_file['url_name'][index])
 
  WebDriverWait(browser, 300).until(
    EC.presence_of_element_located((By.CLASS_NAME,"public-DraftStyleDefault-block"))
  )
  time.sleep(1)
  title_input =  browser.find_element_by_xpath('//div[contains(@class, "public-DraftStyleDefault-block")]/span')
  title_input.send_keys(upload_file['file_name'][index][0:39])

  if isElementExist(browser, '.select-value--3XRKF'):
    category_select = browser.find_element_by_class_name('select-value--3XRKF')
    category_select.click()
    knowledge = browser.find_element_by_xpath('//*[contains(text(),"体育")]')
    knowledge.click()

  timing = browser.find_elements_by_class_name('one-line--3sqFc')[1]
  timing.click()
  
  dist_time = browser.find_element_by_class_name('semi-input-default')
  time.sleep(1)
  time_stamp = datetime.datetime.now() + datetime.timedelta(hours = 1 * index + 2.1)
  hours = int(time_stamp.strftime('%H'))
  if hours > 23 or hours < 9:
    gap = (32 - hours) % 24
    index_add = index_int % 8
    time_stamp = datetime.datetime.now() + datetime.timedelta(hours = 1 * index + 2.1 + gap + index_add * 0.3)
    index_int = index_int + 1
  month_time = time_stamp.strftime('%m')
  day_time = time_stamp.strftime('%d')
  hour_time = time_stamp.strftime('%H')
  minute_time = time_stamp.strftime('%M')
  current_month = datetime.datetime.now().strftime('%m')
  print('预定的发布时间：' + time_stamp.strftime('%Y-%m-%d %H:%M'))
  dist_time.click()
  time.sleep(2)
  if month_time != current_month:
    next_month = browser.find_elements_by_class_name('semi-button semi-button-primary semi-button-borderless semi-button-with-icon just-icon')[1]
    next_month.click()
  time_dom = browser.find_elements_by_class_name('semi-datepicker-switch-text')
  time_dom[0].click()
  target_day = browser.find_element_by_xpath('//div[@class="semi-datepicker-day-main"]/span[text()="' + day_time + '"]')
  target_day.click()
  time_dom[1].click()
  target_hour = browser.find_element_by_xpath('//div[@class="semi-scrolllist-item-wheel undefined-list-hour"]/div[@class="semi-scrolllist-list-outer"]/ul/li[contains(text(),"' + hour_time + '")]')
  target_hour.click()
  target_minute = browser.find_element_by_xpath('//div[@class="semi-scrolllist-item-wheel undefined-list-minute"]/div[@class="semi-scrolllist-list-outer"]/ul/li[contains(text(),"' + minute_time + '")]')
  target_minute.click()
  time.sleep(1)
  
  distribute = browser.find_element_by_xpath('//button[contains(text(),"发布")]')
  distribute.click()
  time.sleep(2)

  if index == 0 and isElementExist(browser, '.icon--1x02I'):
    time.sleep(2)
    bind_button = browser.find_element_by_class_name('icon--1x02I')
    bind_button.click()

    time.sleep(5)
    close_icon = browser.find_element_by_class_name('icon--3ap82')
    close_icon.click()
# browser.quit()