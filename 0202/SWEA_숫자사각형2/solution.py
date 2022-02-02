import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T + 1):
    lst = list(map(int, input().split()))
    H, M = lst[0], lst[1]
    print(f"#{i}")
    for num1 in range(1, H+1):
        for num2 in range(M):
            print(num1 + H*num2, end = ' ')
        print()