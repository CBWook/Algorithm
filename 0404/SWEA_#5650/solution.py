import sys
sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

op_d = [1, 0, 3, 2]

block_d = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2]
}


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    wormhole = [[] for _ in range(11)]

    # 웜홀 위치 찾기
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                wormhole[arr[i][j]].append((i, j))

    # print(wormhole)
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                sr, sc = i, j
                for k in range(4):
                    nr, nc = sr + dr[k], sc + dc[k]
                    d = k
                    cnt = 0
                    while True:
                        if 1 <= arr[nr][nc] <= 5:
                            d = block_d[arr[nr][nc]][d]
                            nr += dr[d]; nc += dc[d]
                            cnt += 1

                            if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 범위 밖(벽)
                                d = op_d[k]
                                nr += dr[d]
                                nc += dc[d]
                                cnt += 1

                        elif 6 <= arr[nr][nc] <= 10:
                            for hole in wormhole[arr[nr][nc]]:
                                if nr != hole[0] or nc != hole[1]:
                                    nr = hole[0]; nc = hole[1]

                        elif arr[nr][nc] == 0:
                            nr += dr[d]; nc += dc[d]

                            if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 범위 밖(벽)
                                d = op_d[k]
                                nr += dr[d]
                                nc += dc[d]
                                cnt += 1

                        if nr == sr and nc == sc:
                            break
                        if arr[nr][nc] == -1:
                            break
                    if max_cnt < cnt:
                        max_cnt = cnt
    print(max_cnt)
