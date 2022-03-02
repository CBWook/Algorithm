import sys
sys.stdin = open('4880.txt', 'r')

def who_win(lwin, rwin):
    if lst[lwin] == 1 and lst[rwin] == 3:
        return lwin
    elif lst[lwin] == 3 and lst[rwin] == 1:
        return rwin
    elif lst[lwin] < lst[rwin]:
        return rwin
    else:
        return lwin

def card(s, e):
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        lwin = card(s, mid)
        rwin = card(mid + 1, e)
        return who_win(lwin, rwin)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{test_case} {card(0, N-1) + 1}')