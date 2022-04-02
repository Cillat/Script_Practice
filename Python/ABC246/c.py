n,k,x = map(int, input().split())
a = list(map(int, input().split()))


result = 0
bigx = []
smallx = []
nokori =[]

for i in range(n):
    if a[i] >= x:
        bigx.append([a[i],a[i]//x])

    else:
        smallx.append(a[i])
    
for j in range(len(bigx)):
    if k - bigx[j][1] >= 0:
        smallx.append(bigx[j][0] - bigx[j][1]*x)
        k -= bigx[j][1]
    else:
        nokori.append(bigx[j][0])

if k == 0:
    for m in range(len(smallx)):
        if m < len(nokori):
            result += nokori[m]

        result += smallx[m]

else:
    sortedsmallx = sorted(smallx, reverse=True)
    for l in range(k, len(sortedsmallx)):
        result += sortedsmallx[l]
        
print(result)