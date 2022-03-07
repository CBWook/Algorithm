import sys
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10**4)
N = int(input())
arr = [list(input()) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = cnt_RG = 0
def DFS(r, c):
    visited[r][c] = 1
    color = arr[r][c]
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            if arr[nr][nc] != color:
                continue
            DFS(nr, nc)
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS(i, j)
            cnt += 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS(i, j)
            cnt_RG += 1
print(cnt, cnt_RG)
