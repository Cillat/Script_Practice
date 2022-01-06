n,q = map(int,input().split())
tall_list = list(map(int,input().split()))

compare_cm = []

for i in range(q):
    compare_cm.append(int(input()))

tall_list.sort(reverse=True)

tmp = 0
tmp_count = 0

next_tmp = 0
next_count = 0

for j in range(q):
    count = tmp_count
    for k in range(tmp ,len(tall_list)):
        if compare_cm[j] <= int(tall_list[k]):
            count += 1
            if j != q-1:
                if compare_cm[j+1] <= int(tall_list[k]):
                    next_tmp = k
                    next_count += 1
        else:

            break
    print(count)
    if j != q-1:
        if compare_cm[j] >= compare_cm[j+1]:
            if k == q-1:
                tmp = k+1
                tmp_count = count
            else:
                tmp = k
                tmp_count = count 
        else:
            if j != q-2:
                if compare_cm[j+1] <= compare_cm[j+2]:
                    tmp = 0
                    tmp_count = 0
                    next_tmp = 0
                    next_count = 0
                else:
                    tmp = next_tmp
                    tmp_count = next_count-1
