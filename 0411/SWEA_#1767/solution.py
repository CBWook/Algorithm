import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def DFS(r, c, d, length):
    global m, max_cnt, cnt, min_len

    print('cnt', cnt)
    print('length', length)
    for ii in range(N):
        for jj in range(N):
            print(arr[ii][jj], end = ' ')
        print()
    print('------------------------')


    if max_cnt < cnt:
        max_cnt = cnt
        min_len = length

    if max_cnt == cnt:
        min_len = min(min_len, length)

    if arr[r][c] == 1:
        visited[r][c] = 0
        cur_cnt = 0
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 > nr or nr >= N or 0 > nc or nc >= N:
                if m == M - 1 and arr[nr][nc] == 0:
                    print('cnt', cnt)
                    for ii in range(N):
                        for jj in range(N):
                            print(arr[ii][jj], end=' ')
                        print()
                    print('------------------------')
                    if max_cnt < cnt + 1:
                        max_cnt = cnt + 1
                        min_len = length + 1
                    if max_cnt == cnt + 1:
                        min_len = min(min_len, length + 1)
                    return
                m += 1
                cnt += 1
                DFS(core_pos[m][0], core_pos[m][1], 0, length)
                cnt -= 1
                m -= 1
                return
            elif arr[nr][nc] == 2: continue
            elif arr[nr][nc] == 1:
                cur_cnt += 1
                print('cur_cnt', cur_cnt)
            elif arr[nr][nc] == 0:
                arr[nr][nc] = 2
                DFS(nr, nc, k, length + 1)
                arr[nr][nc] = 0
        if cur_cnt == 4:
            for n in range(4):
                nnr, nnc = r + dr[n], c + dc[n]
                if not visited[nnr][nnc]:
                    DFS(nnr, nnc, 0, length)
        visited[r][c] = 0
    else:
        nr, nc = r + dr[d], c + dc[d]
        if 0 > nr or nr >= N or 0 > nc or nc >= N:
            if m == M - 1 and arr[nr][nc] == 0:
                if max_cnt < cnt + 1:
                    max_cnt = cnt + 1
                    min_len = length + 1
                if max_cnt == cnt + 1:
                    min_len = min(min_len, length + 1)
                return

            m += 1
            cnt += 1
            DFS(core_pos[m][0], core_pos[m][1], 0, length)
            cnt -= 1
            m -= 1
            return
        elif arr[nr][nc] == 1 or arr[nr][nc] == 2:
            return

        arr[nr][nc] = 2
        DFS(nr, nc, d, length + 1)
        arr[nr][nc] = 0



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    core_pos = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                core_pos.append((i, j))

    M = len(core_pos)
    visited = [[0]*N for _ in range(N)]
    max_cnt = m = cnt = length = 0
    min_len = 0xfffffffff

    DFS(core_pos[m][0], core_pos[m][1], 0, 0)

    print(min_len)
