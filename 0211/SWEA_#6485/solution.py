import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnts = [0]*(5000+1)
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnts[i] += 1
    P = int(input())
    stop_lst = []
    for j in range(P):
        C = int(input())
        stop_lst.append(cnts[C])
    print(f"#{test_case}", end = ' ')
    for stop in stop_lst:
        print(stop, end = ' ')
    print()