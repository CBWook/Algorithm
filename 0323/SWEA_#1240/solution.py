import sys
sys.stdin = open('input.txt', 'r')

pass_lst = [
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1]
]

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end = ' ')
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j]:
                sr, sc = i, j
                flag = True
                break
            if flag:
                break
    ans = []
    for s in range(sc, sc - 7*8, -7):
        pw = arr[sr][s - 6 : s + 1]
        for i, lst in enumerate(pass_lst):
            if pw == lst:
                ans = [i] + ans
    code = 0
    for m in range(len(ans) - 1):
        if m % 2:
            code += ans[m]
        else:
            code += ans[m] * 3
    if (code + ans[7]) % 10:
        print(0)
    else:
        print(sum(ans))

