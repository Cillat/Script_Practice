x1,y1,x2,y2 = map(int, input().split())
flag = 0


for cx in range(x1 - 2, x1 + 3):
    if flag == 0:
        for cy in range(y1 - 2, y1 + 3):
            if pow(cx,2) - 2 * cx * x1 - 2 * cy * y1 + pow(cy,2) == 5 - pow(x1,2) - pow(y1,2):
                if pow(cx,2) - 2 * cx * x2 - 2 * cy * y2 + pow(cy,2) == 5 - pow(x2,2) - pow(y2,2):
                    flag = 1
                    break

if flag == 0:
    print("No")
elif flag == 1:
    print("Yes")



