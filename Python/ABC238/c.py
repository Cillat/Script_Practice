n = input()
n_len = len(n)
n_len_plus = n_len
n = int(n)

tmp = 0
sum = 0
if n_len != 1:
    while n_len_plus != 1:
        tmp += (( 9 * pow(10,n_len_plus-2)) * ( 9 * pow(10,n_len_plus-2) + 1)) // 2
        n_len_plus -= 1
        
    #for i in range(n - pow(10, n_len-1) + 1):
    sum += ((n-pow(10,n_len-1)+1) * (n-pow(10,n_len-1)+2)) // 2

else:
    for j in range(n):
        sum += j + 1

result = (sum + tmp) % 998244353

print(result)



