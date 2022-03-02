import sys
sys.stdin = open('input.txt', 'r')

V = int(input())
E = int(input())
G = [[] for _ in range(V+1)]
visited = [0]*(V+1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def dfs(G, v, visited):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(G, w, visited)
dfs(G, 1, visited)
print(visited.count(1)-1)