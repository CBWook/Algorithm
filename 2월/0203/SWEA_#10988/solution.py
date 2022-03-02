import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    NK_lst = list(map(int, input().split()))
    N, K = NK_lst[0], NK_lst[1]
    num_lst = list(map(int, input().split()))
    # 정렬
    for i in range(len(num_lst)):
        for j in range(i, len(num_lst)):
            if num_lst[i] > num_lst[j]:
                tmp = num_lst[i]
                num_lst[i] = num_lst[j]
                num_lst[j] = tmp
    num_lst = list(set(num_lst))
    print(f'#{test_case} {num_lst[K-1]}')