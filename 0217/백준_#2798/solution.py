import sys
sys.stdin = open('input.txt', 'r')

# n, M = map(int, sys.stdin.readline().split())
# cards = list(map(int, sys.stdin.readline().split()))
# close = 0
# for i in range(1 << n):
#     cnt = 0
#     idx_lst = []
#     for j in range(n):
#         if i & 1 << j:
#             cnt += 1
#             idx_lst.append(j)
#     if cnt == 3:
#         total = 0
#         for idx in idx_lst:
#             total += cards[idx]
#         if total <= M:
#             if M - total < M - close:
#                 close = total
# print(close)
# 시간초과 -> 모든 경우의 수를 돌아서 그런가?


N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
close = 0
total = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:
                if M - total < M - close:
                    close = total
print(close)