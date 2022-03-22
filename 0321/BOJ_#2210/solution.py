import sys
sys.stdin = open('input.txt', 'r')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def DFS(r, c, lst):
    global cnt
    if len(lst) == 6:
        if lst not in order_lst:
            order_lst.append(lst)
            cnt += 1
        return
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < 5 and 0 <= nc < 5:
            DFS(nr, nc, lst + arr[nr][nc])


arr = [list(input().split()) for _ in range(5)]
order_lst = []
cnt = 0
for i in range(5):
    for j in range(5):
        DFS(i, j, arr[i][j])
print(cnt)
