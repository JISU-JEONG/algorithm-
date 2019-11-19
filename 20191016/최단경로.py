import sys
from collections import deque
sys.stdin = open('input.txt','r')

def BFS(s):
    D = [0xfffffff]*(V+1)
    Q = deque()
    D[s] = 0
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            if D[u]+w < D[v]:
                D[v] = D[u] + w
                Q.append(v)
    print(D)

V, E = map(int,input().split())
G = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v,w))
    G[v].append((u, w))

BFS(0)