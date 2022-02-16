import sys
sys.stdin = open('input.txt', 'r')

T = 10
for _ in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ladder_cnt = 0
    start_idx = []
