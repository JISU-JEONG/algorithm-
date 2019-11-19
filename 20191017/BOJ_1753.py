from queue import PriorityQueue
import sys
input = sys.stdin.readline

INF = 0xffffff

V, E = map(int,input().split())
s = int(input())
G = [[] for _ in range(V+1)]
D= [INF]*(V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    G[u].append((v,w))
D[s] = 0
visit =[0]*(V+1)
Q = PriorityQueue()
Q.put((0,s))

while not Q.empty():
    d,u =Q.get()
    if D[u] < d: continue
    visit[u] =1
    for v,w in G[u]:
        if not visit[v] and D[v] > D[u]+w:
            D[v] = D[u]+w
            Q.put((D[v],v))
for i in range(1,V+1):
    if D[i] == INF:
        D[i] ='INF'
    print(D[i])