
lst = [5, 5, 7]
# print(lst[1: 3])
N = len(lst)
bits = [0] * N
max_num = 0
C = 10

def powerset(n):
    nonlocal max_num
    if n == N:
        total_lst = []
        for i in range(len(bits)):
            if bits[i] == 1:
                total_lst.append(lst[i])
        if sum(total_lst) <= C:
            total = 0
            for l in total_lst:
                total += l**2

            if max_num < total:
                max_num = total


        return
    bits[n] = 1
    powerset(n + 1)
    bits[n] = 0
    powerset(n + 1)

powerset(0)
print(max_num)