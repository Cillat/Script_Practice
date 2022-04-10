n = int(input())
s = []

for i in range(n):
    s.append(input().split())

flag = 0

if n == 2:
    if s[0][0] == s[1][0] or s[0][0] == s[1][1]:
        if s[0][1] == s[1][0] or s[0][1] == s[1][1]:
            flag = 1
else:
    for j in range(n):
        if flag == 1:
            break
        else:
            for k in range(j+1,n):
                if s[j][0] == s[k][0] or s[j][0] == s[k][1]:
                    for l in range(k+1,n):
                        if s[j][1] == s[l][0] or s[j][1] == s[l][1]:
                            flag = 1
                            break

        
if flag == 1:
    print("No")
else:
    print("Yes")
