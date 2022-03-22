import sys
sys.stdin = open('input.txt', 'r')

# def DFS(v, m):
#     global cnt
#     global max_cnt
#     if max_cnt < cnt:
#         max_cnt = cnt
#
#     visited[v] = 1
#
#     for w in G[v]:
#         if not visited[w] and w not in G[m]:
#             cnt += 1
#             DFS(w, v)
#             cnt -= 1
#
# N = int(input())
# G = [[] for _ in range(N + 1)]
# while True:
#     u, v = map(int, input().split())
#     if u == -1 and v == -1: break
#     G[u].append(v)
#     G[v].append(u)
#
# scores = [0] * N
# for v in range(1, N + 1):
#     visited = [0] * (N + 1)
#     cnt = 0
#     max_cnt = 0
#     DFS(v, 0)
#     scores[v - 1] = max_cnt
#
# candi_lst = []
# for i in range(len(scores)):
#     if min(scores) == scores[i]:
#         candi_lst.append(i + 1)
# print(min(scores), len(candi_lst))
# candi_lst.sort()
# print(*candi_lst)

from collections import deque

def BFS(v):
    visited = [0] * (N + 1)
    max_dist = 0
    Q = deque()
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                # print('w : ', w, 'visit:', visited[w] - 1)
                if max_dist < visited[w] - 1:
                    max_dist = visited[w] - 1
                Q.append(w)
    return max_dist

N = int(input())
G = [[] for _ in range(N + 1)]
while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1: break
    G[u].append(v)
    G[v].append(u)

scores = [0] * N
for v in range(1, N + 1):
    v_dist = BFS(v)
    scores[v - 1] = v_dist

candi_lst = []
for i in range(len(scores)):
    if min(scores) == scores[i]:
        candi_lst.append(i + 1)
print(min(scores), len(candi_lst))
candi_lst.sort()
print(*candi_lst)