import sys
sys.stdin = open('input.txt', 'r')

### 백트래킹 조합 ###

# # 4개의 원소 중 2개 선택
# lst = [1, 2, 3, 4]
# N = len(lst)
# S = []
# for i in range(N):
#     S.append(lst[i])
#     for j in range(i+1, N): # 이 부분이 반복
#         S.append(lst[j])    #
#         print(S)            #
#         S.pop()             #
#     S.pop()
# print('=====================')
# 재귀로 짜보기
def comb(r, start):
    if r == n:
        print(*S)
    else:
        for i in range(start, N):
            S.append(lst[i])
            comb(r + 1, i + 1)
            S.pop()

while True:
    nums = list(map(int, input().split()))
    N = nums[0]
    lst = nums[1:]
    if N == 0:
        break
    n = 6
    S = []
    comb(0, 0)
    print()
