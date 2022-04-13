
def solution(places):
    answer = []
    for p in places:
        arr = []
        for i in range(5):
            arr.append(list(p[i]))

        person_pos = []
        for r in range(5):
            for c in range(5):
                if arr[r][c] == 'P':
                    person_pos.append((r, c))


        from collections import deque

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        def BFS(sr, sc):
            nonlocal res

            Q = deque()
            Q.append((sr, sc))


            visited[sr][sc] = 1

            while Q:
                r, c = Q.popleft()


                for ii in range(5):
                    for jj in range(5):
                        print(visited[ii][jj], end = ' ')
                    print()
                print('-------------')

                if arr[r][c] == 'P' and abs(visited[r][c] - visited[sr][sc]) == 1:
                    res = 0
                    return
                elif arr[r][c] == 'P' and abs(visited[r][c] - visited[sr][sc]) == 2:
                    if r - sr == -2:
                        if arr[sr - 1][sc] != 'X':
                            res = 0
                            return
                    elif r - sr == 2:
                        if arr[sr + 1][sc] != 'X':
                            res = 0
                            return
                    elif c - sc == 2:
                        if arr[sr][sc + 1] != 'X':
                            res = 0
                            return
                    elif c - sc == -2:
                        if arr[sr][sc - 1] != 'X':
                            res = 0
                            return
                    elif r - sr == -1 and c - sc == 1:
                        if arr[sr - 1][sc] != 'X' or arr[sr][sc + 1] != 'X':
                            res = 0
                            return
                    elif r - sr == 1 and c - sc == 1:
                        if arr[sr + 1][sc] != 'X' or arr[sr][sc + 1] != 'X':
                            res = 0
                            return
                    elif r - sr == 1 and c - sc == -1:
                        if arr[sr + 1][sc] != 'X' or arr[sr][sc - 1] != 'X':
                            res = 0
                            return
                    elif r - sr == -1 and c - sc == -1:
                        if arr[sr - 1][sc] != 'X' or arr[sr][sc - 1] != 'X':
                            res = 0
                            return

                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and visited[r][c] + 1 < 4:
                        visited[nr][nc] = visited[r][c] + 1
                        Q.append((nr, nc))


        res = 1
        for person in person_pos:
            visited = [[0] * 5 for _ in range(5)]
            BFS(person[0], person[1])

        answer.append(res)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))