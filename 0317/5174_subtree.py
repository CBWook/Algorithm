import sys
sys.stdin = open('5174.txt', 'r')

def subtree(v):
    global cnt
    if v:
        cnt += 1
        subtree(ch1[v])
        subtree(ch2[v])

def subtree_size(v):
    global cnt
    if v == 0:
        return
    cnt += 1
    subtree_size(ch1[v])
    subtree_size(ch2[v])

def subtree_size(v):
    if v == 0:
        return 0
    l = subtree_size(ch1[v])
    r = subtree_size(ch2[v])
    return l + r + 1


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 0
    subtree(N)
    print(f'#{test_case} {cnt}')
    print(subtree_size(N))