import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
S =[0] + list(range(1, N+1))
res = []
top = 0
for _ in range(N):
    n = int(input())
    cnt = 0
    if n in S:
        if n > S[top]:
            while S[top] != n:
                top += 1
                cnt += 1
            for _ in range(cnt):
                res.append('+')
            S.remove(n)
            res.append('-')
            top -= 1
        elif n == S[top]:
            res.append('-')
            S.remove(n)
            top -= 1
        else:
            while S[top] != n:
                top -= 1
                cnt += 1
                S.pop()
            for _ in range(cnt):
                res.append('-')
    else:
        res.append('NO')

if 'NO' in res:
    print('NO')
else:
    for n in res:
        print(n)