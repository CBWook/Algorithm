import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    cnt = 0
    for i in range(1 << 12):
        total = 0
        n = 0
        for j in range(12):
            if i & (1 << j):
                total += A[j]
                n += 1
        if total == K and n == N:
            cnt += 1
    print(f"#{test_case} {cnt}")