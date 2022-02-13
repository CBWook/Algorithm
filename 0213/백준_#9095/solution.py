import sys
n = int(sys.stdin.readline())


def go(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return go(num-1)+go(num-2)+go(num-3)


for _ in range(n):
    result = int(sys.stdin.readline())
    print(go(result))
