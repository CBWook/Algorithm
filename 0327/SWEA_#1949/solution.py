import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c):
    global max_dist
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    Q = deque([(r, c)])

    while Q:
        r, c = Q.popleft()

        if max_dist < visited[r][c]:
            max_dist = visited[r][c]

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] < arr[r][c]:
                if visited[nr][nc] < visited[r][c] + 1:
                    visited[nr][nc] = visited[r][c] + 1

                # for ii in range(N):
                #     for jj in range(N):
                #         print(visited[ii][jj], end = ' ')
                #     print()
                # print('-----------------')
                Q.append((nr, nc))

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0
    start = []
    for i in range(N):
        for j in range(N):
            if max_h < arr[i][j]:
                max_h = arr[i][j]
                start = [(i, j)]
            elif max_h == arr[i][j]:
                start.append((i, j))
    max_dist = 0
    for s in start:
        BFS(s[0], s[1])

    for i in range(N):
        for j in range(N):
            for k in range(1, K + 1):
                arr[i][j] -= k
                for s in start:
                    BFS(s[0], s[1])
                arr[i][j] += k

    print(f'#{test_case} {max_dist}')
