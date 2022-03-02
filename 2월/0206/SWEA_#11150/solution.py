import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case}')
    for num in range(1, N + 1):
        for _ in range(N - num):
            print(' ', end = '')
 
        for _ in range(num):
            print('*', end = '')
        print()