# import sys
# sys.stdin = open('input.txt', 'r')

numbers = [4, 1, 2, 1]
target = 4
# N = len(numbers)
# S = []
# cnt = 0
# ans_lst = []


cnt = 0
def solution(numbers, target):
    answer = 0
    N = len(numbers)
    S = []
    ans_lst = []
    def DFS(v):
        global cnt
        if v == N:
            if sum(S) == target:
                if S not in ans_lst:
                    ans_lst.append(S[:])
                    # print(ans_lst)
                    cnt += 1
            return
        S.append(numbers[v])
        # print(S)
        DFS(v + 1)
        S.pop()
        # print(S)

        S.append(-numbers[v])
        # print(S)
        DFS(v + 1)
        S.pop()
        # print(S)

    DFS(0)
    answer = cnt
    return answer

print(solution(numbers, target))

# def num():
#     a = 0
#     def num1():
#         nonlocal a
#         a = 1
#         def num2():
#             nonlocal a
#             a += 1
#         num2()
#         print(a)
#     num1()
#     print(a)
#     return
#
# num()
