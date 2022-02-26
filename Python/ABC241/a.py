a = list(map(int, input().split()))

tmp = a[0]

for i in range(2):
    tmp = a[tmp]

print(tmp)
