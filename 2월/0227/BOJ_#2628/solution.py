import sys
sys.stdin = open('input.txt', 'r')

x, y = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)