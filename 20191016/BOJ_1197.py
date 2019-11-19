import sys
import queue
input = sys.stdin.readline



N, M = map(int, input().split())

# kruskal 문제풀이 ~!
# p = list(range(N+1))
# G = [tuple(map(int, input().split())) for _ in range(M)]
# def find_set(x):
#     if x != p[x]:
#         p[x] =find_set(p[x])
#     return p[x]
# G.sort(key=lambda x: x[2])
# idx= 0
# choice = []
# S = 0
# while len(choice) < N-1:
#     u, v, w = G[idx]
#     a, b = find_set(u), find_set(v)
#     if a != b:
#         p[b] = a
#         choice.append(G[idx])
#         S += w
#     idx += 1
# print(S)


# prim 문제풀이 for문으로 탐색 ~!
# G = [[] for _ in range(N+1)]
# for _ in range(M):
#     u,v,w = map(int,input().split())
#     G[u].append((v, w))
#     G[v].append((u, w))
#
# visit = [False]*(N+1)
# pi = [0]*(N+1)
# key = [0xffff]*(N+1)
# key[1] = 0
# cnt = N
# S = 0
# while cnt:
#     u, MIN = 0,0xffff
#     for i in range(N+1):
#         if not visit[i] and key[i] < MIN : u, MIN = i, key[i]
#     visit[u] = 1
#     S += key[u]
#     for v,w in G[u]:
#         if not visit[v] and w<key[v]:
#             key[v] = w
#             pi[v] = u
#     cnt-=1
# print(S)

# prim 문제풀이 우선순위 큐 으로 탐색 ~!
G = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    G[u].append((v, w))
    G[v].append((u, w))
Q = queue.PriorityQueue()
visit = [False]*(N+1)
key = [0xffff]*(N+1)
key[1] = 0

Q.put((0,1))

while not Q.empty():
    d,u = Q.get()
    if d>key[u]:continue
    visit[u] = 1

    for v,w in G[u]:
        if not visit[v] and w < key[v]:
            key[v] = w
            Q.put((w,v))

print(sum(key[1:]))
