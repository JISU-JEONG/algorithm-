from queue import PriorityQueue

# kruskal 풀이
# N = int(input())
# pos = [tuple(map(float,input().split())) for _ in range(N)]
# star_link = PriorityQueue()
# for i in range(N):
#     for j in range(i+1,N):
#         star_link.put((((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2)**0.5,i,j))
#
# p = list(range(N))
#
# def find_set(x):
#     if x!=p[x]:
#         p[x] =find_set(p[x])
#     return p[x]
# idx, choice=0,[]
# S = 0
# while len(choice)<N-1:
#     w,u,v = star_link.get()
#     a,b = find_set(u),find_set(v)
#     if a!=b:
#         p[b] = a
#         S += w
#         choice.append((w,u,v))
# print("{:.2f}".format(S))

# prim 문제풀이
# N = int(input())
# pos = [tuple(map(float,input().split())) for _ in range(N)]
# G = [[] for _ in range(N)]
#
# for i in range(N):
#     for j in range(i+1,N):
#         w=((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2)**0.5
#         G[i].append((j,w))
#         G[j].append((i,w))
# visit = [0]*N
# pi = [0]*N
# key = [0xfffff]*N
# key[0] = 0
# cnt = N
# S = 0
# while cnt:
#     u, Min = 0, 0xfffff
#     for i in range(N):
#         if not visit[i] and Min >key[i]: u, Min = i, key[i]
#     visit[u] = 1
#     S+=key[u]
#     for v,w in G[u]:
#         if not visit[v] and w<key[v]:
#             pi[v] = u
#             key[v] = w
#     cnt-=1
# print("{:.2f}".format(S))

# prim 문제풀이+우선순위 큐 사용
N = int(input())
pos = [tuple(map(float,input().split())) for _ in range(N)]
G = [[] for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        w=((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2)**0.5
        G[i].append((j,w))
        G[j].append((i,w))
visit = [0]*N
S = 0
Q = PriorityQueue()
Q.put((0,0))
key = [0xffff]*N
key[0]=0
while not Q.empty():
    d, u = Q.get()
    if d > key[u]: continue
    visit[u] = 1
    S+=d
    for v,w in G[u]:
        if not visit[v] and w < key[v]:
            key[v] = w
            Q.put((key[v],v))
print("{:.2f}".format(S))