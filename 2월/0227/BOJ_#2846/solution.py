import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
heights = list(map(int, input().split()))
heights.append(0)
s = e = res = 0
while e < N:
    if heights[e] >= heights[e + 1]:
        total = heights[e] - heights[s]
        if total > res:
            res = total
        s = e + 1
        e += 1
    else:
        e += 1
if res == sum(heights[:N]):
    print(0)
else:
    print(res)