import sys
sys.stdin = open('input.txt', 'r')

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
