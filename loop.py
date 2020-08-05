from selenium import webdriver
import time

browser = webdriver.Chrome()
i = 0
while i < 10:
  try:
    browser.get('https://en.savefrom.net/18/')
    time.sleep(2)
    print(i)
    i = i + 1
  except ZeroDivisionError as e:
      print('error:', e)