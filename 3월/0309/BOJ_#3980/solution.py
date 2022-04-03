import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(11)]
    pos