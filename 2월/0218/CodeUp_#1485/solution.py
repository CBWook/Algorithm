import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
r, c, n = 0, -1, N*M + 1
rs, cs = N, M
direction = 1
while rs > 0 and cs > 0:
    for _ in range(cs):
        n -= 1
        c += direction
        arr[r][c] = n

    rs -= 1

    for _ in range(rs):
        n -= 1
        r += direction
        arr[r][c] = n

    cs -= 1
    direction = -direction

for num in arr:
    for n in num:
        print(n, end = ' ')
    print()