n = int(input())

result = 0
c = 0

for a in range(1,n):
    c = n//(a * 2)
    for b in range(a,n):
        if b <= c: 
            if a*b*c <= n:
                result+= c - b + 1
                if a == 1:
                    c = c//2
                else:
                    c = n//(a*(b+1))     
        else:
            break
        


print(result)

