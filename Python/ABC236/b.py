n = int(input())
a = list(map(int, input().split()))

check_list = [0] * n 

for i in range(4*n-1):
    tmp = a[i]-1
    check_list[tmp] += 1

for j in range(len(check_list)):
    if check_list[j] == 3:
        result = j+1


print(result)

