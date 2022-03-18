import sys
sys.stdin = open('input.txt', 'r')

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]


# 방향 일치시켜야지 BFS 안 k : 0 -> 3 for문이 맞음
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1] # 하 상 좌 우
opp = [1, 0, 3, 2] # 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2 반대방향

def BFS(N, M, R, C, L):
    Q = []
    Q.append((R, C))
    visited[R][C] = 1
    cnt = 1

    while Q:
        r, c = Q.pop(0)

        if visited[r][c] == L:
            return cnt
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and pipe[arr[r][c]][k] and pipe[arr[nr][nc]][opp[k]]:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = BFS(N, M, R, C, L)
    print(f'#{test_case} {ans}')