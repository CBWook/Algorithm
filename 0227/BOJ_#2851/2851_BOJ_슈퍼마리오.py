import sys
sys.stdin = open('2851_BOJ.txt', 'r')

N = 10
scores = []
for _ in range(N):
    scores.append(int(input()))
scores.append(0)
total = res = 0
for i in range(N):
    total += scores[i]
    if abs(100 - total) < abs(100 - (total + scores[i+1])):
        res = total
        break
    elif abs(100 - total) == abs(100 - (total + scores[i+1])):
        res = total + scores[i+1]
        break
if res:
    print(res)
else:
    print(total)