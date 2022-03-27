import sys
sys.stdin = open('input.txt', 'r')


def powerset(n):
    global first_max_num, first_i, first_sj, first_ej
    if n == L:
        total_lst = []

        for b in range(len(bits)):
            if bits[b] == 1:
                total_lst.append(lst[b])


        if sum(total_lst) <= C:
            # print(total_lst)
            total = 0
            for l in total_lst:
                total += l ** 2

            if first_max_num < total:
                first_max_num = total
                first_i = i
                first_sj = j
                first_ej = j + M - 1

        return

    bits[n] = 1
    powerset(n + 1)
    bits[n] = 0
    powerset(n + 1)

def powerset2(n):
    global second_max_num
    if n == L:
        total_lst = []
        for b in range(len(bits)):
            if bits[b] == 1:
                total_lst.append(lst[b])

        # print(total_lst)
        if sum(total_lst) <= C:
            # print(total_lst)
            total = 0
            for l in total_lst:
                total += l ** 2

            if second_max_num < total:
                second_max_num = total

        return

    bits[n] = 1
    powerset2(n + 1)
    bits[n] = 0
    powerset2(n + 1)


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    first_max_num = first_i = first_sj = first_ej = 0
    first_js = []
    for i in range(N):
        for j in range(N - M + 1):
            if sum(arr[i][j : j + M]) <= C:
                square_total = 0
                for num in arr[i][j : j + M]:
                    square_total += num**2
                if first_max_num < square_total:
                    first_max_num = square_total
                    first_i = i
                    first_sj = j
                    first_ej = j + M - 1
            else:
                lst = arr[i][j : j + M]
                L = len(lst)
                bits = [0] * L
                powerset(0)
    second_max_num = second_i = 0
    for i in range(N):
        for j in range(N - M + 1):
            if first_i == i and first_sj <= j <= first_ej: continue
            if sum(arr[i][j : j + M]) <= C:
                square_total = 0
                for num in arr[i][j : j + M]:
                    square_total += num**2
                if second_max_num < square_total:
                    second_max_num = square_total

            else:
                lst = arr[i][j : j + M]
                # print(lst)
                L = len(lst)
                bits = [0] * L
                powerset2(0)
    print(f'#{test_case} {first_max_num + second_max_num}')




