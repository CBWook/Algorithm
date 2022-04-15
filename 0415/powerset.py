# 모든 부분집합 비트 사용

# N = 4
# bits = [0] * N
# cnt = 0
#
# def powerset(k):
#     global cnt
#
#     if k == N:
#         cnt += 1
#         print(bits)
#         return
#     else:
#         bits[k] = 1
#         powerset(k + 1)
#         bits[k] = 0
#         powerset(k + 1)
#
# powerset(0)
# print(cnt)

# A의 부분집합 합이 K인 부분집합의 개수 구하기
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
K = 30
def powerset(i, total):
    global cnt

    if i == N:
        if total == K:
            cnt += 1
        return
    else:
        powerset(i + 1, total + A[i])
        powerset(i + 1, total)

cnt = 0
powerset(0, 0)
print(cnt)
