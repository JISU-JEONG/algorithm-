from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = 0
star = [tuple(map(int,input().split())) for _ in range(N)]
link = PriorityQueue()
for i in range(N):
    for j in range(i+1,N):
        w = ((star[i][0]-star[j][0])**2+(star[i][1]-star[j][1])**2)**0.5
        link.put((w,i,j))
p =list(range(N))
for i in range(M):
    a,b = map(lambda x:int(x)-1,input().split())
    p[b] = a
def find_set(x):
    if x!=p[x]:
        p[x] = find_set(p[x])
    return p[x]
idx,choice =0 ,[0]*M
while len(choice)<N-1:
    w,u,v = link.get()
    a,b = find_set(u),find_set(v)
    if a!=b:
        p[b] = a
        S+=w
        choice.append((w,u,v))
print("{:.2f}".format(S))

# # prim 방법 -> 시간 초과
# N, M = map(int,input().split())
# star = [tuple(map(int,input().split())) for _ in range(N)]
# G = [[] for _ in range(N)]
# link_star = []
# for _ in range(M):
#     i,j =map(lambda x:int(x)-1,input().split())
#     link_star.append((i,j))
#     link_star.append((j,i))
# for i in range(N):
#     for j in range(i+1,N):
#         if (i,j) not in link_star:
#             w = ((star[i][0]-star[j][0])**2+(star[i][1]-star[j][1])**2)**0.5
#             G[i].append((j,w))
#             G[j].append((i,w))
#         else:
#             G[i].append((j,0))
#             G[j].append((i,0))
# Q = PriorityQueue()
# Q.put((0,0))
# key = [0xffff]*N
# visit=[0]*N
# pi = [0]*N
# key[0] = 0
# S = 0
# while not Q.empty():
#     d, u = Q.get()
#     if d > key[u]: continue
#     visit[u] = 1
#     S+=d
#     for v,w in G[u]:
#         if not visit[v] and w <key[v]:
#             key[v] = w
#             pi[v] = u
#             Q.put((key[v], v))
#
# print("{:.2f}".format(S))