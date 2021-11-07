n = int(input())

num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))


tmp = 0
result = [[] * 1 for z in range(n)]

for j in range(n):
    tmp = num_list[j][0]
    for k in range(tmp):
        result[j].append(num_list[j][k+1])

arr = list(map(list, set(map(tuple, result))))

print(len(arr))