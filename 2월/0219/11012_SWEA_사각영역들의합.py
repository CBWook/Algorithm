import sys
sys.stdin = open('11012.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pos_lst = [list(map(int, input().split())) for _ in range(M)]
    total = 0
    xys = []
    for pos in pos_lst:
        r, c, length = pos[0], pos[1], pos[2]
        for rl in range(length):
            for rc in range(length):
                nr = r + rl
                nc = c + rc
                if 0 <= nr < N and 0 <= nc < N:
                    if [nr, nc] not in xys:
                        xys.append([nr, nc])
    for pos in xys:
        total += arr[pos[0]][pos[1]]
    print(f'#{test_case} {total}')
    