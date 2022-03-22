# import sys
# sys.stdin = open('input.txt', 'r')

s = "123"
def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    N = len(s)
    word = ''
    char = ''
    for i in range(N):
        if s[i] in nums_lst:
            word += s[i]
        else:
            char += s[i]
            if char in nums:
                for j in range(10):
                    if char == nums[j]:
                        word += str(j)
                char = ''
    return int(word)

solution(s)