import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input()))
    N = len(lst)
    num = cnt = 0
    for i in range(N):
        if lst[i] != num:
            cnt += 1
            num = lst[i]
    print(f'#{test_case} {cnt}')


