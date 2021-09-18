s = []
s.append(input())
s.append(input())
s.append(input())

t = input()

tmp = 0
ans = []
answer = []

for i in range(len(t)):
    tmp = int(t[i])
    ans.append(s[tmp-1])

answer = ''.join(ans)
print(answer)