import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c):
    Q = deque()
    S = []
    S.append(arr[r][c])
    Q.append((r, c))
    visited[r][c] = 1

    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and abs(arr[r][c] - arr[nr][nc]) == 1:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                S.append(arr[nr][nc])

    return min(S), len(S)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    num = N * N
    dist = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                tnum, tdist = BFS(i, j)
                if dist < tdist or dist == tdist and num > tnum:
                    dist = tdist
                    num = tnum
    print(f'#{test_case} {num} {dist}')

# A = True
# B = False
#
# if A or A and B:
#     print('True')
# else:
#     print('False')