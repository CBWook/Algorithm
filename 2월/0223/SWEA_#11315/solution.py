import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    di = [0, 1, 0, -1, -1, 1, 1, -1]
    dj = [1, 0, -1, 0, -1, 1, -1, 1]
    breaker = False
    for i in range(N):
        for j in range(N):
            if breaker:
                break
            elif arr[i][j] == 'o':
                for k in range(8):
                    ni = i; nj = j
                    ni += di[k]; nj += dj[k]
                    cnt = 0
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        ni += di[k]; nj += dj[k]
                        cnt += 1
                        if cnt == 4:
                            print('YES')
                            breaker = True
                            break
                    if breaker:
                        break
            else:
                continue
        if breaker:
            break
    if not breaker:
        print('NO')