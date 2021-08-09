n,x = map(int, input().split())
num_list = []
# num_list.append(list(map(int,input().split())))
# list(map(int,input().split()))
num_list = map(int,input().split())
divide = n / 2
money_sum = 0
money = 0

money_sum = sum(num_list)
money = money_sum - divide

if money <= x :
    print("Yes")
else :
    print("No")
