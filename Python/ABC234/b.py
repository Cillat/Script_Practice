n = int(input())
n_list = []
for i in range(n):
    tmp = list(map(int, input().split()))
    n_list.append(tmp)
    n_list[i].append(0)


for j in range(n-1):
    for k in range(j+1,n):
        tmp = pow(abs(n_list[j][0] - n_list[k][0]), 2) + pow(abs(n_list[j][1] - n_list[k][1]), 2)
        if n_list[j][2] < tmp**0.5:
            n_list[j][2] = tmp**0.5

n_list.sort(key = lambda x: x[2])

print(n_list[n-1][2])


