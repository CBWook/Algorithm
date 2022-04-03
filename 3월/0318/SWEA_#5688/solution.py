import sys
sys.stdin = open('input.txt', 'r')


def cube(x):
    global ans
    if x**3 > N:
        ans = -1
        return
    if x**3 > 10**18:
        ans = -1
        return
    if x ** 3 == N:
        ans = x
        return
    if N % 2:
        cube(2 * x + 1)
    else:
        cube(2 * x)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
    cube(1)
    print(f'#{test_case} {ans}')