s = input()
t = input()

check = 0
flag = 0
tmp = 0

result = 1

for i in range(len(s)):
    if s[i] != t[i]:
        if check == 0:
            tmp = i
            check = 1
        elif check == 1 and flag == 0:
            if s[i] == t[tmp] and s[tmp] == t[i]:
                flag = 1
            else:
                 result = 0
                 break
        elif check == 1 and flag == 1:
            result = 0
            break

if result == 1:
    print("Yes")
elif result == 0:
    print("No")

            




