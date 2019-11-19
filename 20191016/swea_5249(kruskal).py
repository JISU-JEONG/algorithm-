
T = int(input())

for t in range(1,T+1):
    V,E = map(int, input().split())
    p = list(range(V+1))
    G = [tuple(map(int,input().split())) for _ in range(E)]
    G.sort(key=lambda x:x[2])
    def find_set(x):
        if x!=p[x]:
            p[x] = find_set(p[x])
        return p[x]
    idx,choice = 0,[]
    S = 0
    while len(choice) < V:
        u,v,w = G[idx]
        a,b = find_set(u),find_set(v)
        if a!=b:
            p[b] = a
            choice.append(G[idx])
            S+=w
        idx+=1
    print("#{} {}".format(t,S))