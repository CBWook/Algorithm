import sys
sys.stdin = open('input.txt', 'r')

def DFS(n, total):
    global ans
    if total >= ans:
        return
    if sum(table[n:]) == 0:
        if ans > total:
            ans = total
        return
    if n >= N:
        if ans > total:
            ans = total
        return
    else:
        if table[n]:
            DFS(n + 1, total + prices[0]*table[n])
            DFS(n + 1, total + prices[1])
            DFS(n + 3, total + prices[2])
        else:
            DFS(n + 1, total)


T = int(input())
for test_case in range(1, T + 1):
    prices = list(map(int, input().split()))
    table = list(map(int, input().split()))
    N = len(table)
    ans = prices[3]
    cnt = 0
    DFS(0, 0)
    print(f'#{test_case} {ans}')
