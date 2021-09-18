# coding: utf-8
# Your code here!

import numpy as np

n = int(input())
num_list = []
for i in range(n-1):
    num_list.append(list(map(int,input().split())))

count = 0
count_pass = 0
pass_n = 0
pass_other = 0
receive_n = 0
flag = 0
finish_list =[]

finish_list = np.full((n,2), 0)

for j in range(n):
    finish_list[j][0] = j


while True:
    count += 1
    count_pass += 1
    if count == num_list[1][pass_n]:
        if pass_n == 0:
            flag = 1
            count_pass = 0
        pass_n += 1
        if finish_list[receive_n][1] == 0:
            finish_list[receive_n][1] = 1
            print(count)
        receive_n += 1

        if finish_list[n-1][1] == 1:
            break
        
    if flag == 1:
        if count_pass == num_list[0][pass_other]:
            for z in range(n):
                if finish_list[z][1] == 0:
                    finish_list[z][1] = 1
                    print(count)
                    break
            count_pass = 0
            pass_other += 1
    
            if finish_list[n-1][1] == 1:
                break

        


