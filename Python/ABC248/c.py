import itertools

n,m,k = map(int,input().split())
count = 0
sum_nums = 0
nums = []
check_nums = []

for i in range(1,m+1):
    nums.append(i)

check_nums = list(itertools.product(nums,repeat=n))

for j in range(len(check_nums)):
    sum_nums = 0
    sum_nums = sum(check_nums[j])
    if sum_nums <= k:
        count += 1

ans = count % 998244353
print(ans)