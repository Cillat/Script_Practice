from cmath import pi


n = int(input())
a  = list(map(int, input().split()))

pizza = [0]

for i in range(n):
    for j in range(len(pizza)):
        pizza[j] += a[i]
    
    pizza.append(0)


for k in range(len(pizza)):
    pizza[k] = pizza[k] % 360

pizza.sort()
pizza.append(360)

max = 0
for l in range(len(pizza) - 1):
    if pizza[l+1] - pizza[l] > max:
        max = pizza[l+1] - pizza[l]

print(max)

