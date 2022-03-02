import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T + 1):
    lst = list(map(int, input().split()))
    H, M = lst[0], lst[1]
    print(f"#{i}")
    for num1 in range(H):
        if num1 % 2: # 홀수
            for num2 in range(1, M + 1):
                print((num1 + 1) * M - num2 + 1, end = ' ')
            print()
        else: # 짝수
            for num2 in range(1, M + 1):
                print(num1 * M + num2, end = ' ')
            print()