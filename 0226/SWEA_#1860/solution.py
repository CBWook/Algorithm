import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()
    i = cnt = 0
    flag = False
    while i != (times[-1]+1):
        i += 1
        if i % M == 0:
            cnt += K
        for t in times:
            if i == t:
                if cnt > 0:
                    cnt -= 1
                else:
                    print('Impossible')
                    flag = True
                    break
            elif t == 0:
                print('Impossible')
                flag = True
                break
        if flag:
            break
    else:
        print('Possible')