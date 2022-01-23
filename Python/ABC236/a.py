s = list(input())
a,b = map(int, input().split())

tmp_a = s[a-1]
tmp_b = s[b-1]

s[a-1] = tmp_b
s[b-1] = tmp_a

result = ''.join(s)
print(result)
