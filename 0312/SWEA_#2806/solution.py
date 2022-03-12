import sys
sys.stdin = open('input.txt', 'r')
dr = [0, 1, 0, -1, 1, -1, 1, -1]
dc = [1, 0, -1, 0, 1, 1, -1, -1]

def DFS(r, N, m):
    global ans
    if r == N:
        # for i in range(N):
        #     for j in range(N):
        #         print(arr[i][j], end = ' ')
        #     print()
        # print('------------')
        ans += 1
        return
    m += 1
    for c in range(N):
        if arr[r][c] == 0:
            arr[r][c] = 1
            for k in range(8):
                nr, nc = r + dr[k], c + dc[k]
                while 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = m
                    nr += dr[k]
                    nc += dc[k]
            # for i in range(N):
            #     for j in range(N):
            #         print(arr[i][j], end=' ')
            #     print()
            # print('--------------------')
            DFS(r + 1, N, m)
            for k in range(8):
                nr, nc = r + dr[k], c + dc[k]
                while 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == m:
                        arr[nr][nc] = 0
                    nr += dr[k]
                    nc += dc[k]
            arr[r][c] = 0
            # for i in range(N):
            #     for j in range(N):
            #         print(arr[i][j], end=' ')
            #     print()
            # print('--------------------')
    m -= 1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    ans = 0
    m = 1
    DFS(0, N, m)
    print(f'#{test_case} {ans}')
