T = int(input())

for t in range(1,T+1):
    V,E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v,w = map(int,input().split())
        G[u].append((v,w))
        G[v].append((u,w))
    pi = [0]*(V+1)
    visit = [0] * (V + 1)
    key = [0xffffff]*(V+1)
    key[0]=0
    cnt = V+1
    while cnt:
        v, Min = 0, 0xffffff
        for i in range(V+1):
            if not visit[i] and key[i]<Min:
                v=i;Min = key[i];
        visit[v] = 1
        for u, w in G[v]:
            if not visit[u] and w <key[u]:
                pi[u] = v
                key[u] = w
        cnt-=1

    print("#{} {}".format(t, sum(key)))
