# a,b = map(int, input().split())

# max = a * 6
# min = a * 1

# if b >= min and b <= max :
#     print("Yes")
# else :
#     print("No")
#-------------------------------------------(a)ここまで
# p = int(input())
# count = 0
# money = 1
# flag = True

# # if 1 <= p and p <= 10 ** 7:
# while flag :
#     money = 1
#     for i in range(1,12):#10000000のときにも対応するため
#         money *= i
#         if money > p :
#             p -= int(money / i)
#             count += 1
#             if p == 0:
#                 flag = False
#             break
        
# print(count)
#-----------------------------------------(b)ここまで

n,k = map(int, input().split())
x = list(map(int, input().split()))
flag = True

for h in range(n) :
    value_list = value_list.append("0")#初期化

for i in range(n) :
    dict1 = dict(zip(x,value_list))

while flag:
    if n <= k :#全員に配る時
        for j in range(n) :
            dict1.value_list() += 1 #文字列0から1に書き換えたかった

        k = k-n
    else:
        break









    