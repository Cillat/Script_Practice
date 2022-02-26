import numpy as np

n = int(input())
s = []

for i in range(n):
    s.append(','.join(list(input())))
    # s.append([','.join(map(lambda x: "{}".format(x), input()))])

check_list_yoko = []
check_list_tate = []
check_list_naname = []
flag = 0

for i in range(n):
    check_list_tate.append([])


# check_list_tate[2].append("aaaaa")
# check_list_tate[2].append("iiii")
# print(check_list_tate)

for j in range(n):
    if flag == 1:
        break
    else:
        check_list_yoko.clear()
        for k in range(n):
            check_list_yoko.append(s[j][k*2])
            check_list_tate[k].append(s[j][k*2])

            if len(check_list_yoko) == 6:
                if check_list_yoko.count("#") >= 4:
                    flag = 1
                    break
                else:
                    check_list_yoko.pop()
            
            if len(check_list_tate[k]) == 6:
                if check_list_tate.count("#") >= 4:
                    flag = 1
                    break
                else:
                    check_list_tate[k].pop()


tmp = n - 6
count = 0
if flag == 0:
    for i in range(-1*tmp,tmp+1):
        if flag == 1:
            break
        else:  
            check_list_naname.clear()
            check_list_naname.append(np.diag(s, k=i))
            for j in range(len(check_list_naname) - 5):
                for l in range(6):
                    if check_list_naname[l] == "#":
                        count += 1
                    
                if count >= 4:
                    flag = 1
                    break
                else:
                    check_list_naname.pop()


# if flag == 0:
#     for i in range(-1*tmp,tmp+1):
#         if flag == 1:
#             break
#         else:
#             check_list_naname.clear()  
#             check_list_naname.append(np.diag(np.fliplr(s), k=i))
#             for j in range(len(check_list_naname) - 5):
#                 for l in range(6):
#                     if check_list_naname[l] == "#":
#                         count += 1
                    
#                 if count >= 4:
#                     flag = 1
#                     break
#                 else:
#                     check_list_naname.pop()


if flag == 1:
    print("Yes")
else:
    print("No")