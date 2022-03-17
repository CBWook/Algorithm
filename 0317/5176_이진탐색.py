import sys
sys.stdin = open('5176.txt', 'r')

def in_order(v):
    global num
    if v > N: return
    in_order(v * 2)
    lst[v] = num; num += 1
    in_order(v * 2 + 1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [0]*(N + 1)
    num = 1
    in_order(1)
    print(f'#{test_case} {lst[1]} {lst[N // 2]}')