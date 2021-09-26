import sys

num = [] 

n = int(input())
num = list(map(int, input().split()))
x = int(input())

num_len = len(num)

sum = 0
count = 0
flag = 0

for i in range(num_len):
    sum += num[i]
    count += 1
    if x < sum:
        flag = 1
        break

if flag == 1:
    print(count)
    sys.exit()


loop_count = x // sum

if 0 < loop_count:
    sum = sum * loop_count
    count = count * loop_count


for j in range(num_len):
    if x < sum:
        break
    sum += num[j]
    count += 1
    

print(count)