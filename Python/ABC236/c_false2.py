n,m = map(int,input().split())
s = list(input().split())
t = list(input().split())

check_point = []
for i in range(len(t)):
    check_point.append(s.index(t[i]))

count = 0
print_count = 0

while count < m:
    if print_count == check_point[count]:
        print("Yes")
        count += 1
    else:
        print("No")
    
    print_count += 1


    
