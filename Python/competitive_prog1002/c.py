n = input()

num = len(n)
tmp_a = 0
tmp_b = 0

if num % 2 == 0:
    tmp_a = num / 2
    tmp_b = num /2
else:
    tmp_a = (num // 2) + 1
    tmp_b = num//2


num_str = []
for i in range(num):
    num_str.append(n[i])

num_sort = sorted(num_str,reverse=True)

result_a = []
result_b = []

for j in range(tmp_a):
    if j == tmp_a -1:
        result_b.append(num_sort[j*2])
        break


    result_a.append(num_sort[j*2 + 1])
    result_b.append(num_sort[j*2])

result = int(''.join(result_a)) * int(''.join(result_b))
print(result)

