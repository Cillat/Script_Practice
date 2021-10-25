n = int(input())

point_list = []

for i in range(n):
    point_list.append((input().split()))

count = 0

for j in range (n):
    for k in range(j,n):
        for l in range(k,n):
            if (point_list[j][0] != point_list[k][0] and point_list[k][0] != point_list[l][0] and point_list[l][0] != point_list[j][0]) or (point_list[j][1] != point_list[k][1] and point_list[k][1] != point_list[l][1] and point_list[l][1] != point_list[j][1]):
                if (int(point_list[j][0]) - int(point_list[k][0]) != int(point_list[k][0]) - int(point_list[l][0])) and (int(point_list[j][1]) - int(point_list[k][1]) != int(point_list[k][1]) - int(point_list[l][1])):
                    count += 1

print(count)
