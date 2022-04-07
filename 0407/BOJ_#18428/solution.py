import sys
sys.stdin = open('input.txt', 'r')

# 모든 X에 대해서 O로 바꿔주는 백트리킹 함수 작성
# O의 개수가 3이 되면
# T의 위치에서 S를 찾는 BFS 함수를 작성

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
arr = [list(input().split()) for _ in range(N)]
check = False

def bfs():

    teacher = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'T':
                teacher.append((i, j))

    while teacher:
        r, c = teacher.pop(0)

        for k in range(4):
            nr, nc = r, c
            while True:
                nr += dr[k]
                nc += dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 'S':
                        return False
                    elif arr[nr][nc] == 'O':
                        break
                else:
                    break
    return True

def search(k):
    global check
    if k == 3:
        if bfs():
            check = True
        return

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                search(k + 1)
                arr[i][j] = 'X'

search(0)
if check:
    print('YES')
else:
    print('NO')