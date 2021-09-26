
n = int(input())

num = [] 
num = list(map(int, input().split()))

x = int(input())

num_len = len(num) - 1


count = 0
count_result = 0
sum = 0

while True:
    sum += int(num[count])
    count += 1
    count_result += 1
    if num_len < count:
        count = 0

    if x < sum:
        break

print(count_result)

