week = ['Monday', 'Tuesday', 'Wednesday']
set_point = 630
turn_wed = 1440
number = int(input())
switch = number * 60

if (set_point + switch) < 0:
    print(week[0])
elif 0 <= (set_point + switch) < turn_wed:
    print(week[1])
else:
    print(week[2])








"""-12:00 +14:00
the reference time point is Tuesday, 10:30 in the morning in London (UTC+00:00)
read the input string containing the number and the sign of this number (for example, +4, -10). Note, however, that there will be no sign if the number is 0. The number is always an integer.
this number is the offset for some time zone.
your program should calculate the day of the week in the time zone for which you were given the offset. The reference time point for your calculations is mentioned above.
output the day of the week in the given time zone.
For example, if the input is -11, then, relatively to London, it's "the day before" in this time zone, that is, it's still Monday, but if the input is +3, then it's Tuesday, the same as in London."""
