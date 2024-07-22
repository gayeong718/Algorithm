N=int(input())
nums = list(map(str,input()))
sum = 0

for num in range(N):
    sum += int(nums[num])

print(sum)