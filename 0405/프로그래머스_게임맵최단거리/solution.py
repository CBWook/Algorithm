
def solution(maps):
    answer = 0
    N = len(maps); M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def BFS(r, c):

        Q = []
        visited[r][c] = 1
        Q.append((r, c))

        while Q:
            r, c = Q.pop(0)
            if r == N -1 and c == M - 1:
                return
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maps[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    Q.append((nr, nc))
    BFS(0, 0)
    if visited[N-1][M-1]:
        answer = visited[N-1][M-1]
    else:
        answer = -1
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# print(len(maps))
print(solution(maps))