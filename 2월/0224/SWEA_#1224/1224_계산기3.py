import sys
sys.stdin = open('1224.txt', 'r')

isp = {
    '*' : 2,
    '+' : 1,
    '(' : 0
}
icp = {
    '*' : 2,
    '+' : 1,
    '(' : 3
}
def calc(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    else:
        return num1*num2
T = 10
for test_case in range(1, T+1):
    N = int(input())
    nums = input()
    S = []
    res = []
    for num in nums:
        if num in isp:
            if S:
                if isp[S[-1]] < icp[num]:
                    S.append(num)
                    continue
                else:
                    while isp[S[-1]] >= icp[num]:
                        res.append(S.pop())
                    S.append(num)
                    continue
            else:
                S.append(num)
                continue
        else:
            if num == ')':
                while S[-1] != '(':
                    res.append(S.pop())
                S.pop()
                continue
            else:
                res.append(num)
                continue
    for op in res:
        if op in isp:
            num1 = S.pop()
            num2 = S.pop()
            S.append(calc(num2, num1, op))
        else:
            S.append(int(op))
    print(f'#{test_case} {S[0]}')
