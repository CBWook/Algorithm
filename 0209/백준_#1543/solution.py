import sys
sys.stdin = open('input.txt', 'r')

docs = list(input())
word = input()
length = len(word)
cnt = 0
while len(docs) > length-1:
    doc_word = ''
    for i in range(length):
        doc_word += docs[i]
    if word == doc_word:
        cnt += 1
        for _ in range(length):
            docs.pop(0)
    else:
        docs.pop(0)
print(cnt)


