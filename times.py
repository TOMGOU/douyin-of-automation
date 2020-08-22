import time
import datetime
import math

now_time = time.time()

print(now_time)
index_int = 0
for index in range(30):
  # if index < 5:
  #   continue
  time_stamp = datetime.datetime.now() + datetime.timedelta(hours = 2 * index)
  hours = int(time_stamp.strftime('%H'))
  if hours > 23 or hours < 9:
    gap = (32 - hours) % 24
    index_add = index_int % 5
    time_stamp = datetime.datetime.now() + datetime.timedelta(hours = 2 * index + gap + index_add * 0.3)
    index_int = index_int + 1
  print('time:' + time_stamp.strftime('%Y-%m-%d %H:%M'))
  # print('日:' + time_stamp.strftime('%d'))
  # print('时:' + time_stamp.strftime('%H'))
  # print('分:' + time_stamp.strftime('%M'))