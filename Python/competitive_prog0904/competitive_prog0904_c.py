n = int(input())
p = list(map(int, input().split()))

ins_p = 0
q = [0] * n
#q = []
remove_zero = []
target = 0

for i in range(n):
    ins_p = int(p[i])
    q.insert(ins_p,i+1)

print(q)

for j in q:
    if j != target:
        remove_zero.append(j) 


L=[str(a) for a in remove_zero]
L=" ".join(L)
print(L)

