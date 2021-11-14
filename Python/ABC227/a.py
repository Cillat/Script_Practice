n,k,a = map(int,input().split())

retuowari = n - a
k_nokori = 0
flag = 0

if k <= retuowari + 1:
    print(a + k - 1)
    flag = 1

k_nokori = k - retuowari - 1
retuowari = n

if flag != 1:
    while True:
        if k_nokori <= retuowari:
            print(k_nokori)
            break
        else:
            k_nokori = k_nokori - retuowari 


        
