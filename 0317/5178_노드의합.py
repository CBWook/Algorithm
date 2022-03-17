import sys
sys.stdin = open('5178.txt', 'r')

def sum_push(c):
    if H[c]:
        p = c // 2
        H[p] += H[c]

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    H = [0] * (N + 1)
    leaf_lst = []
    for _ in range(M):
        node, value = map(int, input().split())
        H[node] = value
        leaf_lst.append(node)
    for i in range(N, 0, -1):
        sum_push(i)
    print(f'#{test_case} {H[L]}')
