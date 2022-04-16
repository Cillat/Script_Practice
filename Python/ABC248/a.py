s = input()
check_num = [0]*10
ans = 0

for i in range(9):
    check_num[int(s[i])] = 1

for j in range(10):
    if check_num[j] == 0:
        ans = j
        break

print(ans)

