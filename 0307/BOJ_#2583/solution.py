import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
M, N, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for _ in range(K):
    left_i, left_j, right_i, right_j = map(int, input().split())
    for i in range(left_i, right_i):
        for j in range(left_j, right_j):
            arr[i][j] = 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = 0
def BFS(r, c):
    global cnt
    S = 1
    visited[r][c] = 1
    Q = deque([(r, c)])
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if arr[nr][nc] == 1:
                    continue
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                S += 1
    cnt += 1
    return S

res = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            res.append(BFS(i, j))
res.sort()
print(cnt)
print(*res)
