
# 중복 순열
# def f(i, N):
#     if i == N:
#         print(S)
#         return
#     else:
#         for j in range(N):
#             S.append(A[j])
#             f(i + 1, N)
#             S.pop()
#
# A = [1, 2, 3]
# S = []
# N = len(A)
# f(0, N)

# N = 3
# A = [0] * N
#
# def f(i, N):
#     if i == N:
#         print(A)
#         return
#     else:
#         for j in range(1, N + 1):
#             A[i] = j
#             f(i + 1, N)
#
# f(0, N)

# 순열
# def f(n, k):
#     if n == k:
#         print(p)
#     else:
#         for i in range(k):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[n] = a[i]
#                 f(n + 1, k)
#                 used[i] = 0
#
# a = [2, 3, 4]
# N = len(a)
# p = [0] * N
# used = [0] * N
# f(0, 3)

# 교환을 통해 순열 생성
# arr = [10, 20, 30]
# N = len(arr)
#
# def perm(k, n):
#     if k == n:
#         print(arr)
#         return
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             # print(arr)
#             perm(k + 1, n)
#             arr[k], arr[i] = arr[i], arr[k]
#
# perm(0, N)

arr = [10, 20, 30]
N = len(arr)
order = [0] * N
used = [0] * N

def perm(k, n):
    if k == n:
        print(order)
    else:
        for i in range(n):
            if used[i]: continue
            used[i] = 1
            order[k] = arr[i]
            perm(k + 1, n)
            used[i] = 0

perm(0, N)