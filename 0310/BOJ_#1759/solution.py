import sys
sys.stdin = open('input.txt', 'r')

# 반복 구조
words = ['a', 't', 'c', 'i', 's', 'm']
S = []
N = len(words)
for i in range(N):
    S.append(words[i])

    for j in range(i + 1, N):
        S.append(words[j])
        for k in range(j + 1, N):
            S.append(words[k])
            for m in range(k + 1, N):
                S.append(words[m])
                vow_cnt = con_cnt = 0
                for word in S:
                    if word in ['a', 'e', 'i', 'o', 'u']:
                        vow_cnt += 1
                    else:
                        con_cnt += 1
                if vow_cnt >= 1 and con_cnt >= 2:
                    print(*S)
                S.pop()
            S.pop()
        S.pop()
    S.pop()

print('-----------------')

# 재귀 구조
n = 4
S = []
def comb(r, start):
    if r == n:
        vow_cnt = con_cnt = 0
        for word in S:
            if word in ['a', 'e', 'i', 'o', 'u']:
                vow_cnt += 1
            else:
                con_cnt += 1
        if vow_cnt >= 1 and con_cnt >= 2:
            print(*S)
    else:
        for i in range(start, N):
            S.append(words[i])
            comb(r + 1, i + 1)
            S.pop()

comb(0, 0)















