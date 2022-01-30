n = int(input())
s = input()
a = [0]


for i in range(n):
    if s[i] == "R":
        a.insert(a.index(i) + 1, i+1)
    elif s[i] == "L":
        a.insert(a.index(i) , i+1)

print(*a)

