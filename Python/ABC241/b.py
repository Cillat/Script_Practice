from sys import flags


n,m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = 0

for i in range(m):
    if b[i] in a:
        tmp = a.index(b[i])
        a.pop(tmp)
    else:
        flag = -1
        break

if flag == 0:
    print("Yes")
else:
    print("No")


