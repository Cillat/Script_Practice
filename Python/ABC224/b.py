h,w = map(int, input().split())

a_list = []

for i in range(h):
        a_list.append((input().split()))
        

flag = 0

for j in range(h-1):
    for k in range (w-1):
        if int(a_list[j][k]) + int(a_list[j+1][k+1]) > int(a_list[j+1][k]) + int(a_list[j][k+1]):
            flag = -1


if flag == 0:
    print("Yes")
elif flag == -1:
    print("No")