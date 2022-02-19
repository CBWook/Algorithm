import sys
sys.stdin = open('11010.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 1, -1]
    dj = [1, 1, -1, -1]
    max_num = 0
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(4):
                ni = i
                nj = j
                while 0 <= ni < N and 0 <= nj < N:
                    total += arr[ni][nj]
                    ni += di[k]
                    nj += dj[k]
            total -= arr[i][j]*3
            if max_num < total:
                max_num = total
    print(f"#{test_case} {max_num}")