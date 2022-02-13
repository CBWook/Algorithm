import sys
sys.stdin = open('input.txt', 'r')

from random import randint

# 완전 탐색으로 안풀면 안되는건가?
N = 9
heights = []
for _ in range(N):
    heights.append(int(input()))

total = 0
for height in heights:
    total += height

for i in range(N-1):
    for j in range(0, N-i-1):
        if heights[j] > heights[j+1]:
            heights[j], heights[j+1] = heights[j+1], heights[j]

i = 0
ans = []
while i < N:
    k = 1
    while i + k < N:
        num = 0
        num += heights[i]
        num += heights[i+k]
        if total - num == 100:
            ans_lst = []
            heights[i] = heights[i+k] = 0
            for height in heights:
                if height != 0:
                    ans_lst.append(height)
            ans.append(ans_lst)
        k += 1
    i += 1
lst = ans[randint(0, len(ans)-1)]
for val in lst:
    print(val)
