import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappop, heappush

N, E = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u].append((v, w))
    G[v].append((u, w))
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
    D = [0xfffff] * (N + 1)
    D[start] = 0
    Q = []
    heappush(Q, (0, start))

    while Q:
        w, u = heappop(Q)

        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(Q, (w, v))

    return D[end]

order_list = [(1, v1, v2, N), (1, v2, v1, N)]
min_dist = 0xfffffff
for order in order_list:
    res = 0
    for i in range(3):
        res += dijkstra(order[i], order[i + 1])

    if res != 0 and min_dist > res:
        min_dist = res

if min_dist == 0xfffffff:
    print(-1)
else:
    print(min_dist)