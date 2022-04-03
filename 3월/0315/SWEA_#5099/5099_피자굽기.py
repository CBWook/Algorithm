import sys
sys.stdin = open('5099.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    idxs = list(range(N))
    rear = 0
    S = []
    i = N
    while idxs:
        if N != 0 and rear % N == 0:
            rear = 0
            for j in idxs:
                C[j] = C[j] // 2

        if C[idxs[rear]] == 0:
            S.append(idxs.pop(rear))
            if i < M:
                idxs.insert(rear, i)
                i += 1
            else:
                rear = rear - 1
        rear += 1
        N = len(idxs)
    print(f'#{test_case} {S[-1] + 1}')