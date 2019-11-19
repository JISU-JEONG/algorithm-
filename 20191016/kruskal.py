import sys

sys.stdin = open('input.txt','r')

V, E = map(int,input().split())
Edge = [tuple(map(int,input().split())) for _ in range(E)] # (u, v, w)

# disjoin-set
p = [x for x in range(V)] # 0~V-1
print(p)
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])  # path-compression
    return p[x]

Edge.sort(key=lambda x:x[2])
MST = []
idx = 0
while len(MST) < V-1:
    u,v,w = Edge[idx]
    a = find_set(u); b = find_set(v)
    if a != b:
        MST.append(Edge[idx])
        p[b] = a
    idx +=1
print(MST)