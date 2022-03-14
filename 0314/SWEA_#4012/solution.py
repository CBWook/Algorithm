import sys
sys.stdin = open('input.txt', 'r')

def comb(r, start, M):
    global min_val
    if r == M:
        lst = nums[:]
        order = []
        order.append(S)
        for s in S:
            lst.remove(s)
        order.append(lst)
        A_lst = order[0]; B_lst = order[1]
        A_total = B_total = 0
        for i in range(M-1):
            for j in range(i + 1, M):
                A_total += arr[A_lst[i]][A_lst[j]]
                A_total += arr[A_lst[j]][A_lst[i]]
        for i in range(M-1):
            for j in range(i + 1, M):
                B_total += arr[B_lst[i]][B_lst[j]]
                B_total += arr[B_lst[j]][B_lst[i]]
        if min_val > abs(A_total - B_total):
            min_val = abs(A_total - B_total)
    else:
        for i in range(start, N):
            S.append(nums[i])
            comb(r + 1, i + 1, M)
            S.pop()

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = list(range(N))
    S = []
    min_val = 200000
    M = N // 2
    comb(0, 0, M)
    print(f'#{test_case} {min_val}')
