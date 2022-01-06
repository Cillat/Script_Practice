n,q = map(int,input().split())
tall_list = list(map(int,input().split()))

compare_cm = []

for i in range(q):
    compare_cm.append([int(input()), i, 0])

tall_list.sort(reverse=True)

compare_cm.sort(key=lambda x: x[0] ,reverse=True)
check_cm = list(compare_cm)


tmp = 0
count = 0



for j in range(q):
    for k in range(tmp ,len(tall_list)):
        if check_cm[j][0] <= int(tall_list[k]):
            count += 1    
        else:
            break
    check_cm[j][2] = count
    if k == len(tall_list)-1:
        tmp = len(tall_list)
    else:
        tmp = k

check_cm.sort(key=lambda x: x[1])
    

for l in range(q):
    print(check_cm[l][2])

