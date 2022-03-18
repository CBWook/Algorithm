import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def BFS(V):
    visited[V] = 1
    Q = deque()
    Q.append(V)

    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                Q.append(w)

    max_dist = max_idx = 0
    for i in range(1, N + 1):
        if max_dist < visited[i] or max_dist == visited[i] and max_idx < i:
            max_dist = visited[i]
            max_idx = i
    return max_idx

T = 10
for test_case in range(1, T + 1):
    N, start = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]

    for i in range(0, N, 2):
        v = lst[i]
        u = lst[i + 1]
        G[v].append(u)
    visited = [0] * (N + 1)
    print(f'#{test_case} {BFS(start)}')

# def BFS(s):
#     q = []
#     v = [0]*101
#
#     q.append(s)
#     v[s] = 1
#     sol = s
#
#     while q:
#         c = q.pop(0)
#         # 정답처리
#         if v[sol] < v[c] or v[sol] == v[c] and sol < c:
#             sol = c
#
#         for j in range(1, 101):
#             if adj[c][j] and v[j] == 0:
#                 q.append(j)
#                 v[j] = v[c] + 1
#     return sol
#
#
# T = 10
# for test_case in range(1, T + 1):
#     N, S = map(int, input().split())
#     lst = list(map(int, input().split()))
#     # [1] lst 연결값을 인접행렬에 저장
#     adj = [[0]*101 for _ in range(101)]
#     for i in range(0, len(lst), 2):
#         adj[lst[i]][lst[i+1]] = 1
#     ans = BFS(S)
#     print(f'#{test_case} {ans}')