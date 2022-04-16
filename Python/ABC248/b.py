a,b,k = map(int,input().split())

sum = a
count = 0

while sum < b:
    sum = sum * k
    count += 1

print(count) 