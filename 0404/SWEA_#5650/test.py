
print((True and False) or False)
print((True or False) and True)
(r, c) = (1, 2)
print(r)
print(c)
if (1, 2) == (r, c):
    print(True)
else:
    print(False)

block_d = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2]
}
print(block_d[1][1])