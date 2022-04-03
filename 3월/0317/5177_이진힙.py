import sys
sys.stdin = open('5177.txt', 'r')

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item

    c = hsize
    p = hsize // 2
    while p:
        if H[p] <= H[c]:
            break
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    H = [0] * (N + 1)
    hsize = 0
    for item in arr:
        push(item)
    total = 0
    p = N // 2
    while p:
        total += H[p]
        p //= 2
    print(f'#{test_case} {total}')