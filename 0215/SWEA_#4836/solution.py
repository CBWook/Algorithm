import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    N_col = int(input())
    box_arr = []
    for _ in  range(N_col):
        box_arr.append(list(map(int, input().split())))
    # print(box_arr)
    # print(len(box_arr))
    cnt = 0
    for box in box_arr:
        for i in range(box[0], box[2] +1):
            for j in range(box[1], box[3] + 1):
                if arr[i][j] == 0 or arr[i][j] == box[4]:
                    arr[i][j] = box[4]
                else:
                    cnt += 1
    print(f"#{test_case} {cnt}")