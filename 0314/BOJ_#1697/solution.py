import sys
sys.stdin = open('input.txt', 'r')

# sys.setrecursionlimit(10**6)
# def cur_pos(n, t):
#     global K
#     global min_t
#     if n < 0 or n > 100000:
#         return
#     if t > min_t:
#         return
#     if n == K:
#         if min_t > t:
#             min_t = t
#         return
#     if n - K > 0:
#         if n - K > abs(min_t - t):
#             return
#         cur_pos(n - 1, t + 1)
#     if n - K < 0:
#         cur_pos(2 * n, t + 1)
#         cur_pos(n + 1, t + 1)
#         cur_pos(n - 1, t + 1)
#
#
# N, K = map(int, input().split())
# min_t = 100000
# cur_pos(N, 0)
# print(min_t)
# print(cnt)


