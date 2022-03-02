import sys
sys.stdin = open('2804_BOJ.txt', 'r')

# A, B = input().split()
# N = len(A)
# M = len(B)
# idx_i = idx_j = 0
# flag = False
# for i in range(N):
#     word = A[i]
#     for j in range(M):
#         if B[j] == word:
#             idx_i = i
#             idx_j = j
#             flag = True
#             break
#     if flag:
#         break
# arr = [['.']*N for _ in range(M)]
# for i in range(N):
#     arr[idx_j][i] = A[i]
# for j in range(M):
#     arr[j][idx_i] = B[j]
# for i in range(M):
#     for j in range(N):
#         print(arr[i][j], end = '')
#     print()


def find(A, B):
    N = len(A)
    M = len(B)
    for i in range(N):
        word = A[i]
        for j in range(M):
            if B[j] == word:
                idx_i = i
                idx_j = j
                return idx_i, idx_j
A, B = input().split()
N = len(A)
M = len(B)
idx_A, idx_B = find(A, B)
arr = [['.']*N for _ in range(M)]
for i in range(N):
    arr[idx_B][i] = A[i]
for j in range(M):
    arr[j][idx_A] = B[j]
for i in range(M):
    for j in range(N):
        print(arr[i][j], end = '')
    print()