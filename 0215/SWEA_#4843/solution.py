import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N):
        minidx = maxidx = i
        if i % 2 == 0:
            max_num = nums[i]
            for j in range(i+1, N):
                if max_num < nums[j]:
                    maxidx = j
                    max_num = nums[j]
            nums[i], nums[maxidx] = nums[maxidx], nums[i]
        else:
            min_num = nums[i]
            for j in range(i+1, N):
                if min_num > nums[j]:
                    minidx = j
                    min_num = nums[j]
            nums[i], nums[minidx] = nums[minidx], nums[i]
    print(f"#{test_case}", end = ' ')
    for k in range(10):
        print(nums[k], end = ' ')
    print()
