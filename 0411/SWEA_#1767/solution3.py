import sys
sys.stdin = open('input.txt', 'r')


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def DFS(r, c, direction, length, cnt):
    global m, max_cnt, min_len

    if max_cnt < cnt:
        max_cnt = cnt
        min_len = length

    if max_cnt == cnt:
        min_len = min(min_len, length)



    if arr[r][c] == 1:
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 > nr or nr >= N or 0 > nc or nc >= N:
                if m == M - 1:
                    if max_cnt < cnt + 1:
                        max_cnt = cnt + 1
                        min_len = length
                    if max_cnt == cnt + 1:
                        min_len = min(min_len, length)
                    return
                m += 1
                DFS(core_pos[m][0], core_pos[m][1], 0, length, cnt + 1)
                m -= 1
                return
            elif arr[nr][nc] == 1 or arr[nr][nc] == 2: continue

            arr[nr][nc] = 2
            DFS(nr, nc, k, length + 1, cnt)
            arr[nr][nc] = 0
    else:
        nr, nc = r + dr[direction], c + dc[direction]
        if 0 > nr or nr >= N or 0 > nc or nc >= N:
            if m == M - 1:
                if max_cnt < cnt + 1:
                    max_cnt = cnt + 1
                    min_len = length
                if max_cnt == cnt + 1:
                    min_len = min(min_len, length)
                return

            m += 1
            DFS(core_pos[m][0], core_pos[m][1], 0, length, cnt + 1)
            m -= 1
            return
        elif arr[nr][nc] == 1 or arr[nr][nc] == 2: return

        arr[nr][nc] = 2
        DFS(nr, nc, direction, length + 1, cnt)
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
    max_cnt = m = 0
    min_len = 0xffffff

    DFS(core_pos[m][0], core_pos[m][1], 0, 0, 0)

    print(f'#{test_case} {min_len}')