# import sys
# sys.stdin = open('input.txt', 'r')

def solution(id_list, report, k):

    N = len(id_list)
    answer = [0]*N
    G = [[] for _ in range(N)]
    report = list(set(report))
    K_cnts = [0]*N
    for r in report:
        A, B = r.split()
        A_i = B_i = 0
        for i in range(N):
            if id_list[i] == A:
                A_i = i
            if id_list[i] == B:
                B_i = i
                K_cnts[i] += 1
        G[A_i].append(B_i)
    for i in range(N):
        if K_cnts[i] >= k: # 1, 3 [0, , , 0]
            for j in range(N):
                lst = G[j]
                if i in lst:
                    answer[j] += 1
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))

# N = len(id_list)
# G = [[] for _ in range(N)]
# print(N)
# print(G[1])