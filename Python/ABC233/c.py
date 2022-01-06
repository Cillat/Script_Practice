import itertools

n,x = map(int, input().split())
l = []

for i in range(n):
    input_value = list(map(int,input().split()))
    l.append(input_value)

app_list = []
for j in range(n):
    app_list.append([])
    for k in range(len(l[j])):
        if x % int(l[j][k]) == 0:
            app_list[j].append(int(l[j][k]))

pair_set = list(itertools.product(*app_list))

count = 0

for a in range(len(pair_set)):
    tmp = 1
    for b in range(len(pair_set[a])):
        tmp *= pair_set[a][b]
        if b == len(pair_set[a])-1 and tmp == x:
            count += 1

print(count)

