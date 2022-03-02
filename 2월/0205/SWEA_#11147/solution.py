import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    NM_lst = list(map(int, input().split()))
    N, M = NM_lst[0], NM_lst[1]
    print(f'#{test_case}', end = ' ')
    multi_cnt = 1
    num = N
    while num <= M:
        print(num, end=' ')
        multi_cnt += 1
        num = N * multi_cnt
    print()