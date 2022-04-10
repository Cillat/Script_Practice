n = int(input())
s = []

for i in range(n):
    s.append(input().split())

name_list = []
first_name_flag  = 0
last_name_flag = 0
flag = 0


for j in range(n):
    if first_name_flag == 1 and last_name_flag == 1:
        flag = 1
        break
    else:
        for k in range(j+1,n):
            if s[j][0] == s[k][0] or s[j][0] == s[k][1]:
                first_name_flag = 1
            if s[j][1] == s[k][0] or s[j][1] == s[k][1]:
                last_name_flag = 1


if flag == 1:
    print("No")
else:
    print("Yes")