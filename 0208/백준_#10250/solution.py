import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    cnt = w = 0
    for _ in range(W):
        w += 1
        h = 0
        for _ in range(H):
            cnt += 1
            h += 1
            if cnt == N:
                if w < 10:
                    print(str(h) + '0' + str(w))
                else:
                    print(str(h) + str(w))
        

    
