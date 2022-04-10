def rule(num):
    if num  == 1:
        return 1
    else:
        res = str(rule(num-1)) + " " + str(num) + " " + str(rule(num-1))
        return res


n = int(input())
if n == 1:
    result = 1
elif n == 2:
    result = "1" + " " + "2" + " " + "1"
else:
    result = rule(n-1) + " " + str(n) + " " + rule(n-1)
print(result)












