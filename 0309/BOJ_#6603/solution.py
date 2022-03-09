import sys
sys.stdin = open('input.txt', 'r')

def comb(k, n, lst):
    if k == n:
        if sum(bits) == 6:
            order = []
            for i in range(n):
                if bits[i]:
                    order.append(nums[i])
            lst.append(order)
    else:
        bits[k] = 0
        comb(k + 1, n, lst)
        bits[k] = 1
        comb(k + 1, n, lst)


while True:
    nums = list(map(int, input().split()))
    k = nums.pop(0)
    N = len(nums)
    bits = [0]*N
    if k == 0:
        break
    lst = []
    comb(0, N, lst)
    lst.sort()
    for l in lst:
        print(*l)
    print()
