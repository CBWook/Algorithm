import sys
sys.stdin = open('input.txt', 'r')


nums = list(map(int, input()))
N = len(nums)
for i in range(N):
    for j in range(0, N-i-1):
        if nums[j] <nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
for num in nums:
    print(num, end='')
