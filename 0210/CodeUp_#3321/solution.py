import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A, B = map(int, input().split())
C = int(input())
Di = []
for _ in range(N):
    Di.append(int(input()))

for i in range(N):
    for j in range(N-i-1):
        if Di[j] > Di[j+1]:
            Di[j], Di[j+1] = Di[j+1], Di[j]

prices = []
for k in range(0, N+1):
    cal = C
    for i in range(k):
        cal += Di[N-1-i]

    price = A + k*B
    prices.append(cal//price)

max_val = prices[0]
for price in prices:
    if max_val < price:
        max_val = price

print(max_val)
