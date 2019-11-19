from queue import PriorityQueue
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        s,e,c = map(int,input().split())
        G[s].append((e,c))
    Min = 0xffffff
    for i in range(1,N+1):
        D = [0xffff]*(N+1)
        D[i] = 0
        Q = PriorityQueue()
        Q.put((0,i))
        visit=[0]*(N+1)
        while not Q.empty():
            w,u = Q.get()
            if w > D[u]: continue
            visit[u] = 1
            for v,w in G[u]:
                if not visit[v] and D[v] > D[u]+w:
                    D[v] = D[u]+w
                    Q.put((D[v],v))
        for j in range(1,N+1):
            if D[j]==0xffff:continue
            for k in range(len(G[j])):
                if G[j][k][0] == i:
                    Min = min(Min, D[j]+G[j][k][1])
    if Min ==0xffffff:
        print("#{} -1".format(t))
    else:
        print("#{} {}".format(t,Min))
