import sys
sys.stdin = open('input.txt', 'r')

dr = [1, 0, 0]
dc = [0, 1, -1]

import sys
sys.setrecursionlimit(10**6)
def DFS(r, c, dist, cnt):
    global min_dist, flag

    if not flag:
        visited[r][c] = 1

        if dist >= min_dist:
            return

        if r == N - 1 and c == M - 1:
            min_dist = dist
            flag = True
            return

        for k in range(3):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] == 1 and cnt == 0:

                    arr[nr][nc] = 0
                    visited[nr][nc] = 1

                    DFS(nr, nc, dist + 1, 1)

                    arr[nr][nc] = 1
                    visited[nr][nc] = 0

                if arr[nr][nc] == 0:
                    visited[nr][nc] = 1
                    DFS(nr, nc, dist + 1, cnt)
                    visited[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
min_dist = 123456789
flag = False
DFS(0, 0, 1, 0)
if min_dist == 123456798:
    print(-1)
else:
    print(min_dist)
