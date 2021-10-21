n = int(input())

shop = []


for i in range(n):
    name,point = input().split()
    shop.append((name,point,i+1))

shop.sort(key = lambda x: x[0])


for j in range(n):
    for k in range (j+1,n):
        if shop[j][0] == shop[k][0]:
            if int(shop[j][1]) < int(shop[k][1]):
                shop[j], shop[k] = shop[k], shop[j]
          

for l in range(n):
    print(shop[l][2])

