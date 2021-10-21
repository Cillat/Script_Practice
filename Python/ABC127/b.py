r,d,x = map(int,input().split())

sum = r * x - d
print(sum) 

for i in range(1,10):
    sum = r * sum - d
    print(sum)