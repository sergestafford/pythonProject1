# задача со Stepik про программистов
s = int(input())

if s in [11, 12, 13, 14, 111, 112, 113, 114, 211, 212, 213, 214, 311, 312, 313, 314, 411, 412, 413, 414, 511, 512, 513, 514, 611, 612, 613, 614, 711, 712, 713, 714, 811, 812, 813, 814, 911, 912, 913, 914, 1011, 1012, 1013, 1014]:
  print(str(s) + ' программистов')

elif (s % 10) == 1:
  print(str(s) + ' программист')

elif (s % 10) == 2 or (s % 10) == 3 or (s % 10) == 4:
  print(str(s) + ' программистa')

else:
  print(str(s) + ' программистов')
