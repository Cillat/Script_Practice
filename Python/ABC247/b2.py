n = int(input())
s = []

for i in range(n):
    s.append(input().split())

name_list = []
flag = 0
name_inlist = 0

for j in range(n):
        name_inlist = 0
        if flag == 1:
            break
        elif s[j][0] in name_list and s[j][1] in name_list:
            flag = 1
            break
        else:
            for k in range(j+1,n):
                if flag == 1:
                    break
                else:
                    if s[j][0] == s[k][0] or s[j][0] == s[k][1]:
                        for l in range(j+1,n):
                            if s[j][1] == s[l][0] or s[j][1] == s[l][1]:
                                flag = 1
                                break
                        name_inlist = 1
                        name_list.append(s[j][1])
            if name_inlist == 0:
                name_list.append(s[j][0])


if flag == 1:
    print("No")
else:
    print("Yes")