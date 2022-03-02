import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    max_num = min_num = num_lst[0]
    max_idx = min_idx = 0
    for idx, num in enumerate(num_lst):
        # 최솟값 찾기
        if min_num > num:
            min_num = num
            min_idx = idx
        # 최댓값 찾기
        if max_num <= num:
            max_num = num
            max_idx = idx
    print(f'#{test_case} {abs(max_idx - min_idx)}')