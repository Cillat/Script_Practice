h,w = map(int, input().split())
r,c = map(int, input().split())

if h == 1 and w == 1:
    print("0")
else:
    if h == 1 or w == 1:
        if (r == 1 and c == w) or r == h and c == 1:
            print("1")
        else:
            print("2")
    elif (r == 1 or r == h) and (c == 1 or c == w):
        print("2")
    elif(r == 1 or r == h) or (c == 1 or c == w):
        print("3")
    else:
        print("4")

