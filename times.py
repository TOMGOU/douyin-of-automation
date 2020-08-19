import time
import datetime

now_time = time.time()

print(now_time)

for index in range(10):
  if index < 5:
    continue
  time_stamp = datetime.datetime.now() + datetime.timedelta(hours = 2 * index)
  print('time:' + time_stamp.strftime('%Y-%m-%d %H:%M'))
  print(type(time_stamp.strftime('%Y-%m-%d %H:%M')))