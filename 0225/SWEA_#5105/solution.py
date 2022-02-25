import sys
sys.stdin = open('input.txt', 'r')

def start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i ,j

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(r, c):
    visited = [[0]*N for _ in range(N)]
    Q = []
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        i, j = Q.pop()
        if maze[i][j] == 3:
            return visited[i][j] - 2
        for k in range(4):
            nr = i + dr[k]; nc = j + dc[k]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = visited[i][j] + 1
    return 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sr, sc = start(N)
    print(f'#{test_case} {BFS(sr, sc)}')