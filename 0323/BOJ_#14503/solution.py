import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

check_lst = [(0, -1), (-1, 0), (0, 1), (1, 0)]
cur_lst = [3, 0, 1, 2]
back_lst = [(1, 0), (0, -1), (-1, 0), (0, 1)]

cnt = 1
arr[r][c] = 2
cur_cnt = 0
flag = False

while True:
    cr, cc = r + check_lst[d][0], c + check_lst[d][1]
    if arr[cr][cc] == 0:
        r, c = cr, cc
        d = cur_lst[d]
        cur_cnt = 0
    else:
        d = cur_lst[d]
        cur_cnt += 1
        if cur_cnt == 4:
            br, bc = r + back_lst[d][0], c + back_lst[d][1]
            if arr[br][bc] == 2:
                r, c = br, bc
                cur_cnt = 0
                continue
            elif arr[br][bc] == 1:
                break
        else:
            continue
    arr[r][c] = 2
    cnt += 1

print(cnt)
