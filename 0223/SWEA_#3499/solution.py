import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    N = int(input())
    cards = list(input().split())
    if N % 2:
        for i in range(N//2+1):
            print(cards[i], end = ' ')
            if i + N//2+1 < N:
                print(cards[i+N//2+1], end = ' ')
    else:
        for i in range(N//2):
            print(cards[i], cards[i+N//2], end = ' ')
    print()