import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    home_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home_lst.append((i, j))
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            for K in range(1, 2 * N):
                cnt = 0
                cost = K * K + (K - 1) * (K - 1)
                for lst in home_lst:
                    hr, hc = lst[0], lst[1]
                    if abs(i - hr) + abs(j - hc) + 1 <= K:
                        cnt += 1
                if cost <= M * cnt and max_cnt < cnt:
                    max_cnt = cnt
    print(f'#{test_case} {max_cnt}')

