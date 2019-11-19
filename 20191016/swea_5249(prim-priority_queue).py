import queue

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
    Q = queue.PriorityQueue()
    Q.put((0,0))

    while not Q.empty():
        d, u = Q.get()
        if d > key[u]: continue
        visit[u] = 1
        for v, w in G[u]:
            if not visit[v] and w < key[v]:
                pi[v] = u
                key[v] = w
                Q.put((key[v], v))

    print("#{} {}".format(t, sum(key)))
