import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    i = 0
    pw_lst = []
    while i < N:
        j = 0
        while j < M:
            if arr[i][j] != '0':
                k = j
                while k < M and arr[i][k] != '0':
                    k += 1
                if arr[i][j:k] not in pw_lst:
                    pw_lst.append(arr[i][j:k])
                j = k
            else:
                j += 1
        i += 1
    print(pw_lst)
    print(len(pw_lst[0]))
    bin_pws = []
    for pw in pw_lst:
        bins = ''
        for i in range(len(pw)):
            val = int(pw[i], 16)
            bins += '1' if val & (1 << 3) else '0'
            bins += '1' if val & (1 << 2) else '0'
            bins += '1' if val & (1 << 1) else '0'
            bins += '1' if val & (1 << 0) else '0'
        bin_pws.append(bins)
    print(bin_pws)
