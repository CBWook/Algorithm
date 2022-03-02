import sys
sys.stdin = open('10989.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bomb_pos = [list(map(int, input().split())) for _ in range(M)]
    dr = [0, 0, 1, 0, -1] # 우 하 좌 상
    dc = [0, 1, 0, -1, 0]
    death = 0
    for pos in bomb_pos:
        r, c, bomb = pos[0], pos[1], pos[2]
        for k in range(5):
            nr = r
            nc = c
            for _ in range(bomb):
                nr += dr[k]
                nc += dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    death += arr[nr][nc]
                    arr[nr][nc] = 0
        death += arr[r][c]
    print(f'#{test_case} {death}')

    