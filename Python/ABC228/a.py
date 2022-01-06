s,t,x = map(int, input().split())

if t == 0:
    t = 24

if s < t:
    if s <= x and x < t:
        print("Yes")
    else:
        print("No") 

else:
    if (0 <= x and x < t) or (s <= x and x < 24) :
        print("Yes")
    else:
        print("No")