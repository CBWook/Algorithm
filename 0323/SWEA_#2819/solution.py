import sys
sys.stdin = open('input.txt', 'r')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def DFS(r, c, num):
    global cnt
    if len(num) == 7:
        if num not in ans:
            cnt += 1
            ans.append(num)
        return
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            DFS(nr, nc, num + str(arr[nr][nc]))


T = int(input())
for test_caes in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = []
    cnt = 0
    for i in range(4):
        for j in range(4):
            DFS(i, j, str(arr[i][j]))

    print(f'#{test_caes} {cnt}')