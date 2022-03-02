import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        flag = start = 0
        for i in range(N):
            if arr[i][j] == 1 and start == 0:
                start = 1
            if flag and arr[i][j] == flag:
                cnt += 1
                flag = 0
                start = 0
            elif flag == 0 and start == 1:
                if arr[i][j] == 1:
                    flag = 2
                elif arr[i][j] == 2:
                    flag = 1
    print(f'#{test_case} {cnt}')
