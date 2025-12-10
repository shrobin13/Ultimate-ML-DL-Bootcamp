import math

hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

for_h = (hour + (minute/60)) * 30
for_min = minute * 6

angle = math.fabs(for_h - for_min)

print(f"Minimum Angle : {min(angle, (360 - angle))}")
