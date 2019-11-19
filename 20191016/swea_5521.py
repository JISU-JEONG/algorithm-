T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    G = [[] for _ in range(N+1)]
    F = [0]*(N+1)
    for _ in range(M):
        u,v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    for w in G[1]:
        F[w] = 1
    for i in range(2,N+1):
        if F[i] ==1:
            for w in G[i]:
                if F[w]==1:continue
                F[w] = 2
    cnt = 0
    for i in range(2,N+1):
        if F[i]>=1:
            cnt+=1

    print("#{} {}".format(t,cnt))