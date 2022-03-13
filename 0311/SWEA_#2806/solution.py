import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 1, 0, -1, 1, -1, 1, -1]
dc = [1, 0, -1, 0, 1, 1, -1, -1]

def DFS(r, N):
    global ans

    if r == N:
        cnt = 0
        for i in range(N):
            for j in range(N):
                print(arr[i][j], end = ' ')
            print()
        print('----------------------- ')
        return
    else:
        for c in range(N):
            if arr[r][c] == 0:
                arr[r][c] = 1
                for k in range(8):
                    nr, nc = r + dr[k], c + dc[k]
                    while 0<= nr < N and 0 <= nc < N:
                        arr[nr][nc] = 2
                        nr += dr[k]
                        nc += dc[k]
                DFS(r + 1, N)
                for k in range(8):
                    nr, nc = r + dr[k], c + dc[k]
                    while 0<= nr < N and 0 <= nc < N:
                        arr[nr][nc] = 0
                        nr += dr[k]
                        nc += dc[k]
                arr[r][c] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    ans = 0
    DFS(0, N)
    print(f'#{test_case} {ans}')