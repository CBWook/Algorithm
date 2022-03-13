import sys
sys.stdin = open('input.txt', 'r')

def comb(r, start, M):
    if r == M:
        bits = [0] * M
        lst = nums[:]
        order = []
        order.append(S)
        for s in S:
            lst.remove(s)
        order.append(lst)
        A_lst = order[0]; B_lst = order[1]
        A_total = 0
        subset(0, M, A_lst, bits, A_total)
        print(A_total)
    else:
        for i in range(start, N):
            S.append(nums[i])
            comb(r + 1, i + 1, M)
            S.pop()

def subset(k, n, lst, bits, total):
    if k == n:
        if sum(bits) == 2:
            for i in range(n):
                if bits[i]:
                    total += lst[i]
    else:
        bits[k] = 0
        subset(k + 1, n, lst, bits, total)
        bits[k] = 1
        subset(k + 1, n, lst, bits, total)

# nums = [1, 2, 3]
# N = len(nums)
# bits = [0]*N
# total = 0
# subset(0, N, nums)
#
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = list(range(N))
    S = []
    M = N // 2
    comb(0, 0, M)
