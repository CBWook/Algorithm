import sys
sys.stdin = open('input.txt', 'r')

arr = [list(map(int, input().split())) for _ in range(25)]
new_arr = [[0]*25 for _ in range(25)]
# 좌 우 상 하 대각 1, 2, 3, 4
di = [0, 0, -1, 1, -1, -1, 1, 1]
dj = [-1, 1, 0, 0, -1, 1, -1, 1]
N = 25
for i in range(N):
    for j in range(N):
        total = 0
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj <N:
                total += arr[ni][nj]
        if total == 3:
            new_arr[i][j] = 1
        elif total >= 4 or total <= 1:
            new_arr[i][j] = 0
        elif total == 2 or total == 3:
            if arr[i][j] == 1:
                new_arr[i][j] = 1

for i in range(25):
    for j in range(25):
        print(new_arr[i][j], end= ' ')
    print()