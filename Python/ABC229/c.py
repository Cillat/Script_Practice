n,w = map(int,input().split())

cheese = []

for i in range (n):
    cheese.append((tuple(map(int,input().split()))))

cheese.sort(key = lambda x: x[0], reverse = True)

cheese_delicious = 0
cheese_sum = 0
cheese_select = 0
finish_flag = 0

for j in range (n):
    if finish_flag == 1:
        break
    else:
        cheese_select = cheese[j][1]
        for k in range(cheese_select):
            if cheese_sum + 1 > w:
                finish_flag = 1
                break
            else:
                cheese_sum += 1
                cheese_delicious += cheese[j][0] 

print(cheese_delicious)