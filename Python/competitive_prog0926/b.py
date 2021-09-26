k = int(input())

num = []
num = list(map(int, input().split()))
ans = []


for i in range(2):
    tmp = str(num[i])
    num_len = len(tmp)
    count = len(tmp) - 1
    sum = 0
    for j in range (num_len):
        sum += int(tmp[j]) * pow(k,count)
        count -= 1

    ans.append(int(sum))

answer = ans[0] * ans[1]

print(answer)

