import sys
sys.stdin = open('2953_BOJ.txt', 'r')

total = res = 0
for i in range(1, 6):
    scores = list(map(int, input().split()))
    if res < sum(scores):
        res = sum(scores)
        max_idx = i
print(max_idx, res)
