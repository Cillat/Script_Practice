a_str,b_str = input().split()

a_length = len(a_str)
b_length = len(b_str)

a = list(a_str)
b = list(b_str)

flag = 0
sabun = abs(a_length - b_length)

if a_length >= b_length:
    for s in range(sabun):
        b.insert(0,0)
    for i in reversed(range(0, a_length)):
        if int(a[i]) + int(b[i]) >= 10:
            flag = 1
else:
    for t in range(sabun):
        a.insert(0,0)
    for j in reversed(range(0, b_length)):
        if int(a[j]) + int(b[j]) >= 10:
            flag = 1

if flag == 1:
    print("Hard")
else:
    print("Easy")
