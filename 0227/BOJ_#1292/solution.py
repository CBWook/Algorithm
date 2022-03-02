import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
n = 0
while B > n*(n+1)/2:
    n += 1
nums = []
for i in range(1, n):
    for _ in range(i):
        nums.append(i)
m = int(B - n*(n-1)/2)
for _ in range(m):
    nums.append(n)
res = sum(nums[A-1:])
print(res)