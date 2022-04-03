import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c):

    visited[r][c] = 1
    Q = deque([(r, c)])
    while Q:
        r, c = Q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc]:
                    if visited[nr][nc] > visited[r][c] + arr[nr][nc]:
                        visited[nr][nc] = visited[r][c] + arr[nr][nc]
                        Q.append((nr, nc))
                else:
                    visited[nr][nc] = visited[r][c] + arr[nr][nc]
                    Q.append((nr, nc))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    BFS(0, 0)
    print(f'#{test_case} {visited[N-1][N-1] - 1}')