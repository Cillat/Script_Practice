n = int(input())
s = list(map(int, input().split()))

a = 1
b = 1
area =  0
count = 0
area_list = []

result = 0

for a in range(1,1000):
    for b in range(1,1000):
        area = 4*a*b + 3*a + 3*b
        if area > 1000:
            break
        else:
            area_list.append(area)
            count += 1


for i in range(n):
    for j in range(count):
        if s[i] == area_list[j]:
            result += 1
            break

print(n - result)

