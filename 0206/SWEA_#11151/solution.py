import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    max_num = num_lst[0] + num_lst[1]
    for i in range(N-1):
        num = num_lst[i] + num_lst[i+1]
        if max_num < num:
            max_num = num
    print(f'#{test_case} {max_num}')