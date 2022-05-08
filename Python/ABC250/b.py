n, a, b = map(int, input().split())

s = []
changecount = 0
change_flag = 0
a_count = 0

b_count = 0

if n == 1:
    for l in range(b):
        s.append(".")
    
    result = ''.join(s)
    for m in range(a):
        print(result)

else:
    for i in range(a * n):
        s.append([])
        changecount = change_flag
        for j in range(b * n):
            b_count += 1
            if(changecount % 2 == 0):
                s[i].append(".")
            else:
                s[i].append("#")
            
            if b_count == b:
                b_count = 0
                changecount += 1
                
        a_count += 1
        if a_count == a:
            change_flag += 1
            a_count = 0

    for k in range(a * n):
        result = ''.join(s[k])
        print(result)
