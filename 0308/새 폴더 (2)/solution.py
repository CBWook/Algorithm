# import sys
# sys.stdin = open('input.txt', 'r')

from collections import deque
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
visited = [[0]*3 for _ in range(4)]
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def BFS(r, c, num, keypad):
    visited = [[0] * 3 for _ in range(4)]
    Q = deque([(r, c)])
    visited[r][c] = 1

    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < 4 and 0 <= nj < 3 and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if keypad[ni][nj] == num:
                    return visited[ni][nj]

def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    L_pos = (3, 0)
    R_pos = (3, 2)
    pos_dict = {
        1 : (0, 0),
        2 : (0, 1),
        3 : (0, 2),
        4 : (1, 0),
        5 : (1, 1),
        6 : (1, 2),
        7 : (2, 0),
        8 : (2, 1),
        9 : (2, 2),
        0 : (3, 1)
    }
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            L_pos = pos_dict.get(num)
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            R_pos = pos_dict.get(num)
        else: # 가운데 숫자
            L_dist = BFS(L_pos[0], L_pos[1], num, keypad)
            R_dist = BFS(R_pos[0], R_pos[1], num, keypad)
            if L_dist > R_dist:
                answer += 'R'
                R_pos = pos_dict.get(num)
            elif R_dist > L_dist:
                answer += 'L'
                L_pos = pos_dict.get(num)
            else:
                if hand == 'right':
                    answer += 'R'
                    R_pos = pos_dict.get(num)
                else:
                    answer += 'L'
                    L_pos = pos_dict.get(num)
    return answer

print(solution(numbers, hand))