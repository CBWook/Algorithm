import sys
sys.stdin = open('input.txt', 'r')

def DFS(n, ssum):
    global ans

    if ssum >= B + ans:
        return

    if n == N:
        if ssum >= B and ans > ssum - B:
            ans = ssum - B
        return
    DFS(n + 1, ssum + S[n])
    DFS(n + 1, ssum)


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    ans = 123456489
    DFS(0, 0)
    print(f'#{test_case} {ans}')