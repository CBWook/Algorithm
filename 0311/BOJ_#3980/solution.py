import sys
sys.stdin = open('input.txt', 'r')

def DFS(r, total):
    global max_num
    if r == 11:
        if max_num < total:
            max_num = total
        return
    for c in range(11):
        if arr[r][c] != 0 and visited[c] == 0:
            visited[c] = 1
            DFS(r + 1, total + arr[r][c])
            visited[c] = 0

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [0]*11
    max_num = 0
    DFS(0, 0)
    print(max_num)


