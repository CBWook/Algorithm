import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
S = [0]*K
top = -1
for _ in range(K):
    N = int(input())
    if N:
        top += 1
        S[top] = N
    else:
        S[top] = 0
        top -= 1
print(sum(S))