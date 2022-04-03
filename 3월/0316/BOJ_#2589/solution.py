import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(r, c):
    global max_dist
    visited[r][c] = 1
    Q = deque()
    Q.append((r, c))
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 'L':
                visited[nr][nc] = visited[r][c] + 1
                # for i in range(N):
                #     for j in range(M):
                #         print(visited[i][j], end= ' ')
                #     print()
                # print('-------------------')
                if max_dist < visited[nr][nc]:
                    max_dist = visited[nr][nc] - 1
                Q.append((nr, nc))

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
max_dist = 0
flag = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            cnt = 0
            for k in range(4):
                ni, nj = i + dr[k], j + dc[k]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'L':
                    cnt += 1
            if cnt > 2:
                continue
            else:
                visited = [[0]*M for _ in range(N)]
                BFS(i, j)
print(max_dist)

