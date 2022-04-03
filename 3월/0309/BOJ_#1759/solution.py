import sys
sys.stdin = open('input.txt', 'r')

L, C = map(int, input().split())
chars = list(input().split())
chars.sort()
N = len(chars)
bits = [0]*N

def comb(k, n, L):
    if k == n:
        if sum(bits) == L:
            password = ''
            for i in range(N):
                if bits[i]:
                    password += chars[i]
            con_cnt = vow_cnt = 0
            for p in password:
                if p in ['a', 'e', 'i', 'o', 'u']:
                    vow_cnt += 1
                else:
                    con_cnt += 1
            if vow_cnt >= 1 and con_cnt >= 2:
                ans.append(password)
    else:
        bits[k] = 0
        comb(k + 1, n, L)
        bits[k] = 1
        comb(k + 1, n, L)

ans = []
comb(0, N, L)
ans.sort()
for a in ans:
    for word in a:
        print(word, end='')
    print()
