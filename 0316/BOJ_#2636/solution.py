import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
drr = [0, 1, 0, -1, -1, -1, 1, 1]
dcc = [1, 0, -1, 0, 1, -1, -1, 1]
def BFS(r, c):
    visited[r][c] = 1
    Q = deque()
    Q.append((r, c))
    m = 2
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == 1:
                for k in range(8):
                    nnr, nnc = nr + drr[k], nc + dcc[k]
                    if 0 <= nr < N and 0 <= nc < M and arr[nnr][nnc] == 0:
                        Q.append((nr, nc))
                        visited[nr][nc] = 1
                        for i in range(N):
                            for j in range(M):
                                print(visited[i][j], end = ' ')
                            print()
                        print('---------------------')
                        break
        arr[r][c] = m

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
BFS(3, 1)
for i in range(N):
    for j in range(M):
        print(arr[i][j], end = ' ')
    print()