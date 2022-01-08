k = int(input())

k_list = list(bin(k))
for k in reversed(range(2,len(k_list))):
    if k_list[k] == "1":
        k_list[k] = 2

k_list.pop(0)
k_list.pop(0)

result = int("".join(map(str,k_list)))


print(result)