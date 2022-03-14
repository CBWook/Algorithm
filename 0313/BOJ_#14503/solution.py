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
flag = False
while True:
    if flag:
        print(cnt)
        break
    else:
        temp_d = d
        for k in range(4):
            if temp_d == k:
                nr, nc = r + dir_dict[temp_d][0], c + dir_dict[temp_d][1]
                if arr[nr][nc] == 0:
                    r, c = nr, nc
                    arr[r][c] = 2
                    cnt += 1
                    d = cur_dict[temp_d]
                    # for i in range(N):
                    #     for j in range(M):
                    #         print(arr[i][j], end=' ')
                    #     print()
                    # print('------------------')
                    break
                else:
                    temp_d = cur_dict[temp_d]
        else:
            nr, nc = r + back_dict[d][0], c + back_dict[d][1]
            if arr[nr][nc] == 2:
                r, c = nr, nc
            else:
                flag = True
for i in range(N):
    for j in range(M):
        print(arr[i][j], end= ' ')
    print()