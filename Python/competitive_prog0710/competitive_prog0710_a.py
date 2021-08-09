a,b = map(int, input().split())
count = 0

if a == b:
    count = 1
elif  b - a == 1:
    count = 2
elif b - a < 0 :
    count = 0
else :
    count = b - a + 1

print(count)