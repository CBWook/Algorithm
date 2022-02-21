import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
S = []
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        S.append(order[1])
    elif order[0] == 'pop':
        if S:
            print(S.pop())
        else:
            print(-1)
    elif order[0] == 'top':
        if S:
            print(S[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(S))
    elif order[0] == 'empty':
        if S:
            print(0)
        else:
            print(1)


