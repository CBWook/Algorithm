import sys
sys.stdin = open('1216.txt', 'r')

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    print(f'#{test_case}', end = ' ')
    words = [list(input()) for _ in  range(100)]
    max_len = 0
    for i in range(100):
        # 행 우선 순회
        # ABCCBAANDB i = 0 j = 0 ... 100
        for j in range(100):
            for M in range(100 - j + 1):
                for k in range(M//2):
                    if words[i][j + k] != words[i][j + M-k-1]:
                        break
                else: # 회문을 찾았을 때
                    if max_len < M:
                        max_len = M
        # 열 우선 순회
        for j in range(100):
            for M in range(1, 100 - j + 1):
                for k in range(M//2):
                    if words[j + k][i] != words[j + M-k-1][i]:
                        break
                else:
                    if max_len < M:
                        max_len = M
    print(max_len)
