import sys
sys.stdin = open('4881.txt', 'r')

def perm(k, N, cur_sum):
    global ans
    if ans <= cur_sum: # 매개변수를 추가해서 하면 깊어지기전에 미리 break
        return
    if k == N:
        # total = 0
        # for k in range(N):
        #     total += arr[k][order[k]]
        # print(cur_sum, total) # 여기서 total을 걸어버리면 미리 함수가 깊어질대로 깊어진 상태에서 계산을 함 -> 걸어주나마나
        if ans > cur_sum:
            ans = cur_sum
    else:
        for i in range(N):
            if visited[i]: continue
            order[k] = cols[i]
            visited[i] = 1
            perm(k+1, N, cur_sum + arr[k][order[k]])
            visited[i] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    order = [0]*N
    cols = [x for x in range(N)]
    ans = 10*N
    perm(0, N, 0)
    print(f'#{test_case} {ans}')