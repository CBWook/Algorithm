import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    for _ in range(N):
        max_heights = min_heights = heights[0]
        max_idx = min_idx = 0
        for i in range(len(heights)):
            if max_heights < heights[i]:
                max_idx = i
                max_heights = heights[i]
            if min_heights > heights[i]:
                min_idx = i
                min_heights = heights[i]
        heights[max_idx] -= 1
        heights[min_idx] += 1

    max_heights = min_heights = heights[0]
    for h in heights:
        if max_heights < h:
            max_heights = h
        if min_heights > h:
            min_heights = h
    print(f"#{test_case} {max_heights - min_heights}")