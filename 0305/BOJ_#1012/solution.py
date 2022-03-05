import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def DFS(r, c):
    visited[r][c] = 1
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 0 or visited[nr][nc] == 1:
                continue
            DFS(nr, nc)

T = int(input())
for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                DFS(i, j)
                cnt += 1
    print(cnt)