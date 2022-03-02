import sys
sys.stdin = open('input.txt', 'r')

# 점화식 정의
def a_n(n):
    a = 8 + 12*(n-1) + 3*(n-1)*(n-2)
    return a
N = int(input())
if N == 1:
    print(1)
elif N <= 7:
    print(2)
else:
    dist = 1
    while True:
        if N < a_n(dist):
            print(dist+1)
            break
        else:
            dist += 1
