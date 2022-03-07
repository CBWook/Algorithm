import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# for k in range(H):
#     for i in range(N):
#         for j in range(M):
#             print(arr[k][i][j], end = ' ')
#         print()
#     print('----------')
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
di = [0, 1, 0, -1, 0, 0]

dj = [1, 0, -1, 0, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

def BFS(start):
    global max_cnt
    for k, i, j in start:
        visited[k][i][j] = 1
    Q = deque(start)
    while Q:
        k, i, j = Q.popleft()
        for m in range(6):
            nk, ni, nj = k + dk[m], i + di[m], j + dj[m]
            if 0 <= nk < H and 0 <= nj < M and 0 <= ni < N and visited[nk][ni][nj] == 0:
                if arr[nk][ni][nj] == -1:
                    continue
                Q.append((nk, ni, nj))
                visited[nk][ni][nj] = visited[k][i][j] + 1
                if max_cnt < visited[nk][ni][nj]:
                    max_cnt = visited[nk][ni][nj] - 1

def find(H, N, M):
    max_cnt = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if visited[k][i][j] == 0 and arr[k][i][j] != -1:
                    return -1
                if max_cnt < visited[k][i][j]:
                    max_cnt = visited[k][i][j]
    return max_cnt - 1

start = []
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                start.append((k, i, j))
max_cnt = 0
BFS(start)
print(find(H, N, M))
# for k in range(H):
#     for i in range(N):
#         for j in range(M):
#             print(visited[k][i][j], end = ' ')
#         print()
#     print('----------')

