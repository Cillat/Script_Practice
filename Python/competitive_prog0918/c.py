# coding: utf-8
# Your code here!
from collections import OrderedDict

dict = OrderedDict()
name = []
ans = []
ans_num = []
tmp = []

s = input()
n = int(input())

for i in range(n):
    name.append(input())
    

for j in range(len(s)):
    dict[s[j]] = j+1

for k in range(n):
    ans.append(list(name[k]))

print(ans[0])
print(len(ans[0]))

for c in range(n):
    for a in range(1,n):
        for b in range(len(ans[a])):
            if ans[c][b] >= ans[a][b] :
                tmp.append(name[c])
                name[a] = name[c]
                name[c] = tmp.pop()


print(name)
#for k in range(n):
#    print(ans[k])


# わからん