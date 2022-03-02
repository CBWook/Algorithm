import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))
cnt = 0
for i in range(N-1, 0, -1):
    if scores[i] <= scores[i-1]:
        cnt += scores[i-1] - (scores[i] - 1)
        scores[i-1] = scores[i] - 1
print(cnt)
