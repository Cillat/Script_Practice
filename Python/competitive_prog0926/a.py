a,b,c = map(int,input().split())

ans = 0
flag = 0

for i in range(1000):
    ans = c * i
    if a <= ans and ans <= b:
        print(ans)
        flag = 1
        break
    if b < ans:
        break 


if flag == 0:
    print(-1)