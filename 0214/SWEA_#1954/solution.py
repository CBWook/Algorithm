import sys
sys.stdin = open('input.txt', 'r')

T = 10
for _ in range(T):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_num = 0
    # 행 우선순회
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if max_num < sum:
            max_num = sum
    # 열 우선순회
    for j in range(100):
        sum = 0
        for i in range(100):
            sum += arr[i][j]
        if max_num < sum:
            max_num = sum
    # 대각순회(좌측 먼저)
    i = j = sum = 0
    while i < 100:
        sum += arr[i][j]
        i += 1
        j += 1
    if max_num < sum:
        max_num = sum
    # 대각순회(우측 먼저)
    i = sum = 0
    j = 99
    while i < 100:
        sum += arr[i][j]
        i += 1
        j -= 1
    if max_num < sum:
        max_num = sum
    print(f"#{test_case} {max_num}")