import sys
sys.stdin = open('1232.txt', 'r')

op = ['+', '-', '*', '/']


def in_order(v):
    if v > N:
        return
    if H[v]:
        if H[v] not in op:
            return float(H[v])
        l = in_order(L[v])
        r = in_order(R[v])
        if l != None and r != None:
            if H[v] == '+':
                return l + r
            elif H[v] == '-':
                return l - r
            elif H[v] == '*':
                return l * r
            else:
                return l / r

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    H = [''] * (N + 1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    for _ in range(N):
        idx, *arr = input().split()
        H[int(idx)] += arr[0]
        if len(arr) == 2:
            L[int(idx)] = int(arr[1])
        if len(arr) == 3:
            L[int(idx)] = int(arr[1])
            R[int(idx)] = int(arr[2])
    print(f'#{test_case} {int(in_order(1))}')
