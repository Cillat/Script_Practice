n = int(input())

name_list = []

for i in range(n):
    name_list.append(input())

check_list = list(set(name_list))


max_count = 0
for j in range(len(check_list)):
    if max_count < name_list.count(check_list[j]):
        max_name = check_list[j]
        max_count = name_list.count(check_list[j])
    

print(max_name)


