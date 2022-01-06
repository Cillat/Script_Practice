l,r = map(int, input().split())
s = input()

slice_str = s[l-1:r]
slice_str_reverse = slice_str[len(slice_str)::-1]

print(s.replace(slice_str,slice_str_reverse))