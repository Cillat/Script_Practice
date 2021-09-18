a = input()
b = input()
c = input()

name_lis = []
abc_flag = 0
arc_flag = 0
agc_flag = 0
ahc_flag = 0

name_lis.append(a)
name_lis.append(b)
name_lis.append(c)

for i in range(3):
    if name_lis[i] == "ABC":
        abc_flag = 1
    elif name_lis[i] == "ARC":
        arc_flag = 1
    elif name_lis[i] == "AGC":
        agc_flag = 1
    elif name_lis[i] == "AHC":
        ahc_flag = 1

if abc_flag == 0:
    print("ABC")
if arc_flag == 0:
    print("ARC")
if agc_flag == 0:
    print("AGC")
if ahc_flag == 0:
    print("AHC")
