import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end = ' ')
    bin_num = list(input())
    tri_num = list(input())
    N = len(bin_num)
    for i in range(N):
        copy_num = bin_num[:]
        if copy_num[i] == '1':
            copy_num[i] = '0'
        else:
            copy_num[i] = '1'

        num = ''
        for copy in copy_num:
            num += copy
        ans = int(num, 2)

        j = 0
        M = len(tri_num)
        while j < M:
            n = tri_num[j]
            cnt = 0
            nums = tri_num[:]
            while cnt < 2:
                nums[j] = str(n)
                n = (int(n) + 1) % 3
                if nums == tri_num:
                    continue
                num = ''
                for s in nums:
                    num += s
                if ans == int(num, 3):
                    print(ans)
                cnt += 1
            j += 1


