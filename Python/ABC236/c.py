n,m = map(int,input().split())
s = list(input().split())
t = list(input().split())

count = 0

for i in range(len(s)):
    if s[i] == t[count]:
        print("Yes")
        if count != m-1:
            count+= 1 
    else:
        print("No")


    
