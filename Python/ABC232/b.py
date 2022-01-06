s = input()
t = input()

alpha_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
flag = 0
tmp = 0
sabun = 0

for i in range(len(s)):
    s_index = alpha_list.index(s[i])
    t_index = alpha_list.index(t[i])

    if s_index >= t_index:
        sabun = t_index - s_index + 26
    else:
        sabun = t_index - s_index
    if len(s) != 1:    
        if i == 0:
            tmp = sabun
        else:
            if sabun != tmp:
                flag = -1
if len(s) == 1:
    print("Yes")
else:
    if flag == 0:
        print("Yes")
    else:
        print("No")