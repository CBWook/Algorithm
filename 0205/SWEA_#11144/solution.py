import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    num_lst = list(map(int, input().split()))
    cnt = 0
    for num in num_lst:
        cnt += 1
    print(f'#{test_case} {cnt} {num_lst[-1]}')