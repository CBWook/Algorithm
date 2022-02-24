import sys
sys.stdin = open('4874.txt', 'r')

def calc(num1, num2, op):
    if op == '+':
        return num2 + num1
    elif op == '-':
        return num2 - num1
    elif op == '*':
        return num2 * num1
    elif op == '/':
        return num2 // num1
operator = ['+', '-', '*', '/']
T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    nums = list(input().split())
    S = []
    num_cnt = op_cnt = 0
    for i in range(len(nums)):
        if nums[i] in operator:
            op_cnt += 1
            if len(S) > 1:
                num1 = S.pop(); num2 = S.pop()
                S.append(calc(num1, num2, nums[i]))
        else:
            if nums[i] == '.':
                if num_cnt - 1 != op_cnt:
                    print('error')
                else:
                    print(S.pop())
            else:
                num_cnt += 1
                S.append(int(nums[i]))