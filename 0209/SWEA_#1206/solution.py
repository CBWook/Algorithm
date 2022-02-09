import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        heigths = [nums[i-2], nums[i-1], nums[i+1], nums[i+2]]
        max_height = heigths[0]
        for h in heigths:
            if max_height < h:
                max_height = h
        if nums[i] > max_height:
            cnt += nums[i] - max_height
    print(f'#{test_case} {cnt}')
