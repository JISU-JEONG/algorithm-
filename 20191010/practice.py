# 13 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V, E = map(int,input().split())
L = [0] * (V+1)  # tree = [[0, 0, 0] for _ in range(V+1)]
R = [0] * (V+1)  # tree = [[] for _ in range(V+1)]
P = [0] * (V+1)

arr = list(map(int,input().split()))
for i in range(0,E*2,2):
    p,c = arr[i],arr[i+1]
    if L[p] == 0: L[p] = c
    else: R[p] = c
    P[c] = p

#--------------------------------
def inorder(v):
    if v==0:
        return
    print(v, end=' ')
    inorder(L[v])
    inorder(R[v])
#--------------------------------

#--------------------------------
def treeHeight(v, k):
    if v==0:
        return k-1
    if k==3:
        print(v,end=' ')
    h = max(treeHeight(L[v], k+1),treeHeight(R[v], k+1))
    return h
#--------------------------------

#--------------------------------
def treeSize(v):
    global cnt
    if v==0:
        return
    cnt+=1
    treeSize(L[v])
    treeSize(R[v])
#--------------------------------

#--------------------------------
def Ancestor(a, b):
    A = set()
    B = set()
    while P[a] !=0:
        A.add(P[a])
        a = P[a]
    while P[b] !=0:
        B.add(P[b])
        b = P[b]
    return A&B
#--------------------------------

print(L)
print(R)
print(P)
inorder(1)
print()
treeHeight(1, 0)
cnt = 0
treeSize(1)
print()
print(cnt)
print(Ancestor(9,13))