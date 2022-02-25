import sys
sys.stdin = open('1225.txt', 'r')

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    Q = list(map(int, input().split()))
    N = 8
    i = 0
    while True:
        i += 1
        if i % 5:
            tmp = Q[0] - i % 5
        else:
            tmp = Q[0] - 5
        for j in range(1, N):
            Q[j - 1] = Q[j]
        Q[-1] = tmp
        if Q[-1] <= 0:
            Q[-1] = 0
            break
    print(f'#{test_case}', *Q)