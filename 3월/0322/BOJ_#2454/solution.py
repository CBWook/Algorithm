import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

