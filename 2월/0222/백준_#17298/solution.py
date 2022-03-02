import sys
sys.stdin = open('input.txt', 'r')

# N = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
# for i in range(N):
#     for j in range(i+1, N):
#         if nums[i] < nums[j]:
#             print(nums[j], end = ' ')
#             break
#     else:
#         print(-1, end = ' ')
# 시간초과

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
S = []
top = 0
for _ in range(N):
    if S:
        if S[-1] < nums[top]:
            S.append(nums[top])
            top += 1
        else:
            top += 1
    else:
        S.append(nums[top])
print(S)