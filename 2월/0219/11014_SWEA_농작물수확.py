import sys
sys.stdin = open('11014.txt', 'r')

def area(N, arr):
    res = 9*N*N
    for i in range(N-1):
        for j in range(N-1):
            S_lst = []
            S = 0
            for r in range(i+1):
                for c in range(N):
                    S += arr[r][c]
            S_lst.append(S)
            S = 0
            for r in range(i+1, N):
                for c in range(j+1):
                    S += arr[r][c]
            S_lst.append(S)
            S = 0
            for r in range(i+1, N):
                for c in range(j+1, N):
                    S += arr[r][c]
            S_lst.append(S)
            max_S  = 0
            min_S = 9*N*N
            for S in S_lst:
                if max_S < S:
                    max_S = S
                if min_S > S:
                    min_S = S
            if res > max_S - min_S:
                res = max_S - min_S
    return res


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr1 = [[0]*N for _ in range(N)]
    arr2 = [[0]*N for _ in range(N)]
    arr3 = [[0]*N for _ in range(N)]
    ret = area(N, arr)
    # 행렬 회전
    # 시계 90
    for i in range(N):
        for j in range(N):
            arr1[i][j] = arr[N-1-j][i]
    if ret > area(N, arr1):
        ret = area(N, arr1)
    # 180
    arr2[0] = arr[2]
    arr2[1] = arr[1]
    arr2[3] = arr[0]
    if ret > area(N, arr2):
        ret = area(N, arr2)
    # 반시계 90
    for i in range(N):
        for j in range(N):
            arr3[i][j] = arr[j][N-1-i]
    if ret > area(N, arr3):
        ret = area(N, arr3)
    print(ret)

