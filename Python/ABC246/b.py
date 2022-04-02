from cmath import sqrt


import math

a,b = map(int, input().split())

meter = math.sqrt(pow(a,2) + pow(b,2))
gain = 1/meter

print(a*gain, b*gain)