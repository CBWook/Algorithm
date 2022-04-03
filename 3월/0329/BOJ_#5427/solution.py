import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(start, f_start):
    Q = deque()
    for s in start:
        Q.append((s[0], s[1]))
        visited[s[0]][s[1]][0] = 1
        visited[s[0]][s[1]][1] += arr[s[0]][s[1]]

    for f in f_start:
        Q.append((f[0], f[1]))
        visited[f[0]][f[1]][0] = 1
        visited[f[0]][f[1]][1] += arr[f[0]][f[1]]

    while Q:
        r, c = Q.popleft()
        for i in range(N):
            for j in range(M):
                print(visited[i][j], end=' ')
            print()
        print('-------------------')

        if visited[r][c][1] == '@':
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if nr < 0 or nr == N or nc < 0 or nc == M:
                    print(visited[r][c][0])
                    return
                if arr[nr][nc] == '#': continue

                if visited[nr][nc][0] == 0:
                    visited[nr][nc][0] = visited[r][c][0] + 1
                    visited[nr][nc][1] += '@'
                    Q.append((nr, nc))
        elif visited[r][c][1] == '*':
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if arr[nr][nc] == '#': continue
                if 0 <= nr < N and 0 <= nc < M:
                    if visited[nr][nc][1] == '@' and visited[nr][nc][0] < visited[r][c][0] + 1:
                        visited[nr][nc][1] = '*'
                        visited[nr][nc][0] = visited[r][c][0] + 1
                        Q.append((nr, nc))


T = int(input())
T = 2
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    start = []
    f_start = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '@':
                start.append((i, j))

            elif arr[i][j] == '*':
                f_start.append((i, j))

    visited = [[[0, ''] for _ in range(M)] for _ in range(N)]

    BFS(start, f_start)
# M = 3
# visited = [[[0, ''] for _ in range(M)] for _ in range(M)]
# for i in range(M):
#     for j in range(M):
#         print(visited[i][j], end = ' ')
#     print()