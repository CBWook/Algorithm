import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def BFS(r, c):
    global t, pos, size, sr, sc, cnt
    # print('sr, sc', r, c)
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    Q.append((r, c))

    visited[r][c] = 1

    while Q:
        r, c = Q.popleft()

        print('visited')
        for ii in range(N):
            for jj in range(N):
                print(visited[ii][jj], end = ' ')
            print()
        print('---------------------')


        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] <= size:
                if arr[nr][nc] == size or arr[nr][nc] == 0:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                elif arr[nr][nc] < size: # 사이즈보다 작은 물고기
                    cnt += 1
                    arr[nr][nc] = 0
                    t += visited[r][c]
                    sr, sc = nr, nc
                    return


N = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(N)]

# 아기 상어 위치
sr = sc = 0
flag = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sr = i; sc = j
            arr[sr][sc] = 0
            flag = True
            break
    if flag:
        break

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

size = 2; t = 0; cnt = 0

while True:
    tmp_sr, tmp_sc = sr, sc
    BFS(sr, sc)
    if cnt == size:
        size += 1
        cnt = 0
    print('size', size)
    print('cnt', cnt)
    print('t', t)
    if tmp_sr == sr and tmp_sc == sc:
        break
    # print('array')
    # for iii in range(N):
    #     for jjj in range(N):
    #         print(arr[iii][jjj], end=' ')
    #     print()
    # print('----------------------')
    # print('sr,sc', sr, sc)
    # print('size:', size)
    # print('t:', t)


print(t)
