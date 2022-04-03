import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir_dict = {0 : (0, -1), 1 : (-1, 0), 2: (0, 1), 3 : (1, 0)}
cur_dict = {0 : 3, 1 : 0, 2 : 1, 3 : 2}
back_dict = {0 : (1, 0), 1: (0, -1), 2 : (-1, 0), 3 : (0, 1)}
back_cur = {0: 1, 1: 2, 2: 3, 3: 0}
