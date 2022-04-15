# def f(i, j, k):
#     print(i, j, k)
#
# N = 10
# R = 3
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             f(i, j, k)

# 재귀 함수
# def nCr(n, r, s):
#     if r == 0:
#         # print(comb)
#         return
#     else:
#         for i in range(s, n - r + 1):
#             comb[r - 1] = A[i]
#             print(comb)
#             nCr(n, r - 1, i + 1)
#
# n = 5
# r = 3
# k = r
# A = [i for i in range(1, n + 1)]
# comb = [0] * r
# nCr(n, r, 0)

# def nCr(n, r, s, k):
#     if r == 0:
#         # print(comb)
#         return
#     else:
#         for i in range(s, n - r + 1):
#             comb[k - r] = A[i]
#             print(comb)
#             nCr(n, r - 1, i + 1, k)
#
# n = 10
# r = 3
# k = r
# A = [i for i in range(1, n + 1)]
# comb = [0] * r
# nCr(n, r, 0, k)

# arr = 'ABCD'
arr = [1, 2, 3, 4]
N = len(arr)
R = 3
# pick = [0] * R
#
# def comb(k, s):
#     if k == R:
#         # print(pick)
#         return
#     else:
#         for i in range(s, N):
#             pick[k] = arr[i]
#             print(pick)
#             comb(k + 1, i + 1)
#
# comb(0, 0)

pick = []
def comb2(k, s):
    if k == R:
        print('pick:', pick)
        return
    else:
        for i in range(s, N):
            pick.append(arr[i])
            print(pick)
            comb2(k + 1, i + 1)
            pick.pop()

comb2(0, 0)