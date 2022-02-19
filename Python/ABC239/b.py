from unittest import result


x = int(input())

if x/10 >= 1:
    result = x//10
elif x/10 < 1 and x/10 >0:
    result = 0
elif x/10 > -1 and x/10 < 0:
    result = -1
else:
    result = x//10

print(result)


