import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir_dict = {0 : (0, -1), 1 : (-1, 0), 2: (0, 1), 3 : (1, 0)}
cur_dict = {0 : 3, 1 : 0, 2 : 1, 3 : 2}
back_dict = {0 : (1, 0), 1: (0, -1), 2 : (-1, 0), 3 : (0, 1)}
cnt = 1
arr[r][c] = 2
while True:
    for k in range(4):
        if d == k:
            nr, nc = r + dir_dict[k][0], c + dir_dict[k][1]
            if arr[nr][nc] == 0:
                r, c = nr, nc
                arr[r][c] = 2
                d = cur_dict[k]
                cnt += 1
                for i in range(N):
                    for j in range(M):
                        print(arr[i][j], end = ' ')
                    print()
                print(r, c)
                print(d)
                print('-----------------------------')

                break
            else:
                d = cur_dict[d]

    else:
        nr, nc = r + back_dict[d][0], c + back_dict[d][1]
        if arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            break
# print(cnt)
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j], end = ' ')
#     print()
