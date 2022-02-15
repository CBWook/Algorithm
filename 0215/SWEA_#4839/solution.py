import sys
sys.stdin = open('input.txt', 'r')

def binarySearch(N, key):
    start = 1
    end = N
    cnt = 0
    while start <= end :
        md = (start + end) // 2
        if md == key:
            return cnt
        elif md > key:
            end = md
            cnt += 1
        else:
            start = md
            cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T+1):
    end, A, B = map(int, input().split())
    A_cnt = binarySearch(end, A)
    B_cnt = binarySearch(end, B)
    print(f"#{test_case}", end = ' ')
    if A_cnt == B_cnt:
        print(0)
    elif A_cnt > B_cnt:
        print('B')
    else:
        print('A')