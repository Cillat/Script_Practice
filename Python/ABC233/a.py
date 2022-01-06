import math
x,y = map(int,input().split())

if y > x:
    result = math.ceil( ( y - x ) / 10 )
    print(result)

else:
    print(0)