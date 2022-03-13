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
k = -1
flag = False
while True:
    while k < 3:
        k += 1
        nr, nc = r + dir_dict[d][0], c + dir_dict[d][1]
        if arr[nr][nc] == 0:
            r, c = nr, nc
            arr[r][c] = 2
            cnt += 1
            k = -1
            d = cur_dict[d]
            cur_cnt = 0
        else:
            if cur_cnt == 4:
                pass
            else:
                d = cur_dict[d]
                cur_cnt += 1


    nr, nc = r + back_dict[d][0], c + back_dict[d][1]
    if arr[nr][nc] == 1:
        print(d)
        print(nr, nc)
        flag = True
    else:
        r, c = nr, nc
    if flag:
        break
print(cnt)