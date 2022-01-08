k = int(input())

increment = 1
sum = 1
count = 0
while True:
    if sum < k:
        count += 1
        increment *= 2
        sum += increment
    
    else:
        sum -= increment
        break

k -= sum + 1
num_list = [2]

for i in range(count):
    num_list.append(0)

print(num_list)

print(k)
k_list = list(bin(k))

print(k_list)
    
if len(k_list)-1 < len(num_list)-1:
    compare = len(num_list)-1 - len(k_list)-2
    for j in range(compare):
        k_list.insert(-1,0)

for k in reversed(range(2,len(k_list))):
    if k_list[k] == 1:
        num_list[k] = 2

result = int("".join(map(str,num_list)))

print(result)







