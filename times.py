import time
import datetime

now_time = time.time()

print(now_time)

time_stamp = datetime.datetime.now() + datetime.timedelta(hours=1)

print(time_stamp.strftime('%Y-%m-%d %H:%M'))