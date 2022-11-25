import math
s, r = map(float, input().split())
pi = 3.141592
print(round(math.sqrt((pi * r ** 2 - s) / pi), 3))