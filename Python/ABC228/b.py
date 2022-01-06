
n,x = map(int,input().split())
member_list = (list(map(int,input().split())))
member_list.insert(0,0)
 
isKnown = [0] * (n+1)
 
isKnown[x] = 1
 
tmp = member_list[x]
count = 1

for i in range(n):
  if isKnown[tmp] == 0:
    isKnown[tmp] = 1
    tmp = member_list[tmp]
    count += 1
  else:
    break
 
print(count)
  

# n,x = map(int,input().split())
# member_list = (list(map(int,input().split())))
# member_list.insert(0,0)

# count_list = []
# tmp = x
# flag = 0


# count_list.append(tmp)
# tmp_num = 0


# while True:
#     for j in range(len(count_list)):
#         if count_list[j] == member_list[tmp]:
#             flag = 1
#     if flag == 0:
#         count_list.append(member_list[tmp])
#         tmp = member_list[tmp]
#     else:
#         break

# print(len(count_list))



# while True:
#     if flag == 1:
#         break
#     else:
#         if len(count_list) == n:
#             break
#         else:


# count = 0
# for i in range(n):
#     if tmp_num != member_list[tmp]:
#         tmp_num = member_list[tmp]
#         tmp = member_list[tmp]
#         count += 1
#     else:
#         break

# for j in range(n):
#     check = member_list[tmp] in count_list  
#     if check == False:
#         count_list.append(member_list[tmp])
#         tmp = member_list[tmp]
#     else:
#         break



# count = 0
# check_list =[]
# check_list_two =[]
# for i in range(n):
#     check_list.append(count_list[i])
#     if set(check_list_two) != set(check_list):
#         count += 1
#         check_list_two.append(count_list[i])
#     else:
#         break





