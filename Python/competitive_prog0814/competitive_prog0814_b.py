s,t = map(int, input().split())

count = 0
i = 0
j = 0
k = 0

for i in range(101):
        for j in range(101):
            for k in range(101):
                if i+j+k <= s and i*j*k <= t:
                    count += 1
                else:
                    break    

print(count)


