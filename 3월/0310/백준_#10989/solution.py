import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cnts = [0]*(10000+1)
while N:
    num = int(input())
    cnts[num] += 1
    N -= 1
i = 0
while i < 10001:
    while cnts[i] != 0:
        print(i)
        cnts[i] -= 1
        continue
    i += 1
