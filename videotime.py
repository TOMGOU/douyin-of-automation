def isVideoLong(string, times):
  time_list = string.split(':')
  length = len(time_list)
  video_time = 0
  if length == 1:
    video_time = int(time_list[0])
  elif length == 2:
    video_time = int(time_list[0]) * 60 + int(time_list[1])
  else:
    video_time = int(time_list[0]) * 60 * 60 + int(time_list[1]) * 60 + int(time_list[2])
  return video_time < times * 60

print(isVideoLong('15:13', 15))