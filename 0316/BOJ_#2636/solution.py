import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def DFS(r, c):
    visited[r][c] = 1
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == 1:
            for k in range(4):
                ni, nj = nr + dr[k], nc + dc[k]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                    for i in range(N):
                        for j in range(M):
                            print(visited[i][j], end=  ' ')
                        print()
                    print('----------------------')
                    DFS(nr, nc)
                    arr[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
DFS(3, 1)
