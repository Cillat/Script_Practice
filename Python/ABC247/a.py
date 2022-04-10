from unittest import result


s = list(input())
for i in reversed(range(4)):
    if i == 3:
        if s[i] == "1":
            s[i] = "0"
    else:
        if s[i] == "1":
            s[i+1] = "1"
        else:
            s[i+1] = "0"
s[0] = "0"
result = "".join(map(str,s))

print(result)

