import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    total = 0
    for j in range(N):
        total += arr[N//2][j]
    for i in range(N//2):
        for k in range(N//2-i, N//2+i+1):
            total += arr[i][k]
            total += arr[N-1-i][k]
    print(f'#{test_case} {total}')