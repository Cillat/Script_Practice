from itertools import product

n,x = map(int, input().split())
jump = []
flag = 0

for i in range(n):
    jump.append(list(map(int,input().split())))

lst = [list(v) for v in product(*jump)]

for j in reversed(range(len(lst))):
    sum = 0
    for k in range(len(lst[j])):
        sum += lst[j][k]
        if sum > x:
            break
    
    if sum == x:
        flag = 1
        break
if flag == 1:
    print("Yes")
else:
    print("No")





# for i in range(2 ** n):
#     sum = []
#     total = 0
#     for j in range(n):  # このループが一番のポイント
#         if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
#             total += jump[j][1]  # 買い物累計額にも加算
#         sum.append(total)

# print(total)



# check_step_a = [jump[0][0]] * (pow(2,n) // 2)
# check_step_b = [jump[0][1]] * (pow(2,n) // 2)

# count = 2

# for j in range(1,n):
#     devide = 2 * count
#     for k in range((pow(2,n)//divide)):
#         check_step_a[k] += jump[j][0]
#         check_step_b[k] += jump[j][0]
#     for l in range((pow(2,n)//divide),(pow(2,n) * 2//divide)):
#         check_step_a[l] += jump[j][1]
#         check_step_b[l] += jump[j][1]
    
#     count *= 2

# if x in check_step_a or x in check_step_b:
#     print("Yes")
# else:
#     print("No")

