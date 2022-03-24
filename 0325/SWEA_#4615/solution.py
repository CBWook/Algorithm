import sys
sys.stdin = open('input.txt', 'r')

dr = [-2, -1, 0, 1, 2, 1, 0, -1]
dc = [0, 1, 2, 1, 0, -1, -2, -1]

check_lst = [
    [(-1, 0)],
    [(-1, 0), (0, 1)],
    [(0, 1)],
    [(0, 1), (1, 0)],
    [(1, 0)],
    [(1, 0), (0, -1)],
    [(0, -1)],
    [(0, -1), (-1, 0)]
]
stone_lst = [-1, 2, 1]
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2 - 1][N // 2 - 1] = 2
    arr[N // 2][N // 2] = 2
    b_cnt = w_cnt = 2
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
    print('------------')
    for _ in range(M):
        r, c, stone = map(int, input().split())
        r, c = r - 1, c - 1

        if arr[r][c] == 0:

            for k in range(8):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == stone:
                    for check in check_lst[k]:
                        nnr, nnc = r + check[0], c + check[1]
                        if stone == 1:
                            if arr[nnr][nnc] == 2:
                                arr[r][c] = 1
                                arr[nnr][nnc] = 1
                                for i in range(N):
                                    for j in range(N):
                                        print(arr[i][j], end=' ')
                                    print()
                                print('------------')
                                b_cnt += 2
                                w_cnt -= 1
                        if stone == 2:
                            if arr[nnr][nnc] == 1:
                                arr[r][c] = 2
                                arr[nnr][nnc] = 2
                                for i in range(N):
                                    for j in range(N):
                                        print(arr[i][j], end=' ')
                                    print()
                                print('------------')
                                w_cnt += 2
                                b_cnt -= 1
    print(b_cnt, w_cnt)
