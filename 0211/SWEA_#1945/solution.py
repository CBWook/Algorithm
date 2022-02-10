import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = {
        2 : 0,
        3 : 0,
        5 : 0,
        7 : 0,
        11 : 0
    }
    while N != 1:
        for key in nums:
            if N % key == 0:
                N = N // key
                nums[key] += 1
    print(f"#{test_case}", end = ' ')
    for key in nums:
        print(f'{nums.get(key)}', end = ' ')
    print()





