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
                    cnt += 1
            return
        S.append(numbers[v])
        DFS(v + 1)
        S.pop()

        S.append(-numbers[v])
        DFS(v + 1)
        S.pop()

    DFS(0)
    answer = cnt
    return answer

print(solution(numbers, target))