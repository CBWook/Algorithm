import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    lst = list(input().split())
    num1, num2 = int(lst[0]), int(lst[1])
    if lst[-1] == '/':
        result = num1//num2
    elif lst[-1] == '+':
        result = num1 + num2
    elif lst[-1] == '*':
        result = num1 * num2
    else:
        result = num1 - num2
    print(f'#{test_case} {result}')