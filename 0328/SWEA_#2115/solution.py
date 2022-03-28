import sys
sys.stdin = open('input.txt', 'r')

def sqaure_sum(lst):
    total = 0
    for l in lst:
        total += l**2
    return total

def powerset_first(n, total, s_total):
    global first_num, max_idx

    if n == L:
        if total <= C and first_num < s_total:
            first_num = s_total
            max_idx = [(i, j, j + M - 1)]
        return
    else:
        powerset_first(n + 1, total + lst[n], s_total + lst[n]**2)
        powerset_first(n + 1, total, s_total)

def powerset_second(n, total, s_total):
    global second_num

    if n == L:
        if total <= C and second_num < s_total:
            second_num = s_total
        return
    else:
        powerset_second(n + 1, total + lst2[n], s_total + lst2[n]**2)
        powerset_second(n + 1, total, s_total)


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    first_num = 0
    max_idx = []
    for i in range(N):
        for j in range(N - M + 1):
            s_total = 0
            if sum(arr[i][j : j + M]) <= C:
                s_total = sqaure_sum(arr[i][j:j + M])
                if first_num < s_total:
                    first_num = s_total
                    max_idx = [(i, j, j + M - 1)]

            else:
                lst = arr[i][j : j + M]
                L = len(lst)
                powerset_first(0, 0, 0)

    second_num = 0
    for i in range(N):
        for j in range(N - M + 1):
            if i == max_idx[0][0]: continue

            if sum(arr[i][j : j + M]) <= C:
                s_total = sqaure_sum(arr[i][j : j + M])

                if second_num < s_total:
                    second_num = s_total
            else:
                lst2 = arr[i][j : j + M]
                L = len(lst2)
                powerset_second(0, 0, 0)

    print(f'#{test_case} {first_num + second_num}')