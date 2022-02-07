import sys
sys.stdin = open('input.txt', 'r')

# 점화식 정의
def a_n(n):
    return int(1 + (n-1) + 0.5*(n-1)*(n-2))
N = int(input())
if N == 1:
    print('1/1')
else:
    cnt = 1
    while True:
        cnt += 1
        if a_n(cnt-1) <= N <a_n(cnt):
            if cnt % 2 == 0:
                deno = 1
                nume = cnt-1
                for _ in range(N-a_n(cnt-1)):
                    deno += 1
                    nume -= 1
                print(f'{nume}/{deno}')
                break
            else:
                deno = cnt-1
                nume = 1
                for _ in range(N-a_n(cnt-1)):
                    deno -= 1
                    nume += 1
                print(f'{nume}/{deno}')
                break
            