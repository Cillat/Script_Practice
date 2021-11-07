from typing import Counter


s = input()

tmp_s = []
tmp_s.append(s)

print(tmp_s)

pop_s = []
for a in range(len(s)):
    pop_s.append(s[a])

flag = 0


for i in range(1,len(s)):
    change_s = pop_s.pop(0)
    pop_s.append(change_s) 
    result = ''.join(pop_s)

    for j in range(len(tmp_s)):
        if tmp_s[j] == result:
            flag = 1
    
    if flag == 0:
        tmp_s.append(result)
    elif flag == 1:
        flag = 0

print(len(tmp_s))
