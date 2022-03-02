import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def DFS(i, j):
    global cnt
    visited[i][j] = 1
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0 or visited[ni][nj] == 1:
                continue
            cnt += 1
            DFS(ni, nj)

comp_cnt = 0
cnts = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            cnt = 1
            DFS(r, c)
            cnts.append(cnt)
            comp_cnt += 1
print(comp_cnt)
cnts.sort()
for cnt in cnts:
    print(cnt)