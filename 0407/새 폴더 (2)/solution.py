import sys
sys.stdin = open('input.txt', 'r')

# # 상 하 좌 우 (0 1 2 3)
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # 벽 만났을 때
# op_d = [1, 0, 3, 2]
#
# block_d = {
#     1: [1, 3, 0, 2],
#     2: [3, 0, 1, 2],
#     3: [2, 0, 3, 1],
#     4: [1, 2, 3, 0],
#     5: [1, 0, 3, 2]
# }
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     wormhole = [[] for _ in range(11)]
#
#     # 웜홀 위치 찾기
#     for i in range(N):
#         for j in range(N):
#             if 6 <= arr[i][j] <= 10:
#                 wormhole[arr[i][j]].append((i, j))
#
#     max_cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:
#                 sr, sc = i, j # 출발 위치 저장
#                 # 4 방향 탐색
#                 for k in range(4): # k : 0, 1, 2, 3 (상, 하, 좌, 우)
#                     nr, nc = sr + dr[k], sc + dc[k]
#                     d = k # 방향 저장
#                     cnt = 0 # 점수
#                     while True:
#
#                         # 벽
#                         if 0 > nr or nc >= N or 0 > nc or nc >= N:
#                             d = op_d[d]
#                             nr += dr[d]; nc += dc[d]
#                             cnt += 1
#                         # 블록
#                         elif 1 <= arr[nr][nc] <= 5:
#                             d = block_d[arr[nr][nc]][d]
#                             nr += dr[d]; nc += dc[d]
#                             cnt += 1
#                         # 웜홀
#                         elif 6 <= arr[nr][nc] <= 10:
#                             if wormhole[arr[nr][nc]][0] == (nr, nc):
#                                 nr, nc = wormhole[arr[nr][nc]][1]
#                             else:
#                                 nr, nc = wormhole[arr[nr][nc]][0]
#                             nr += dr[d]; nc += dc[d]
#                         # 통행 가능
#                         elif arr[nr][nc] == 0:
#                             nr += dr[d]; nc += dc[d]
#                         # 블랙홀
#                         elif arr[nr][nc] == -1:
#                             break
#
#
#                         if nr == sr and nc == sc:
#                             break
#
#                     if max_cnt < cnt:
#                         max_cnt = cnt
#
#     print(f'#{test_case} {max_cnt}')

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
                        # 벽
                        if 0 > nr or nr >= N or 0 > nc or nc >= N:
                            d = op_d[d]
                            cnt += 1

                        # 블록
                        elif 1 <= arr[nr][nc] <= 5:
                            d = block_d[arr[nr][nc]][d]
                            cnt += 1

                        # 웜홀
                        elif 6 <= arr[nr][nc] <= 10:
                            if wormhole[arr[nr][nc]][0] == (nr, nc):
                                nr, nc = wormhole[arr[nr][nc]][1]
                            else:
                                nr, nc = wormhole[arr[nr][nc]][0]
                        elif arr[nr][nc] == -1:
                            break
                        # 통행가능
                        nr += dr[d]; nc += dc[d]

                        if nr == sr and nc == sc:
                            break

                    if max_cnt < cnt:
                        max_cnt = cnt

    print(f'#{test_case} {max_cnt}')