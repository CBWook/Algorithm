import sys
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10**6)
N = int(input())
arr = [list(input()) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = cnt_RG = 0
visited = [[0]*N for _ in range(N)]
def DFS(r, c):
    visited[r][c] = 1
    color = arr[r][c]
    if color == 'R' or color == 'G':