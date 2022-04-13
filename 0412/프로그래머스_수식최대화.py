def solution(expression):
    answer = 0
    op = ['-', '*', '+']

    lst = []
    num = ''
    for e in expression:
        if e not in op:
            num += e
        else:
            lst.append(num)
            lst.append(e)
            num = ''
    lst.append(num)
    # print(lst)

    def calc(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
    S = []
    used = [0] * 3
    def perm(n, r):
        if n == r:
            for oper in S:

            return

        for i in range(3):
            if used[i]: continue
            used[i] = 1
            S.append(op[i])
            perm(n + 1, r)
            S.pop()
            used[i] = 0

    perm(0, 3)
    return answer

expression = "100-200*300-500+20"
solution(expression)