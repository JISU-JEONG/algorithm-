T = int(input())

def bfs(x):
    visit[x] = 1
    c_queue = [x]
    p_queue = [x]
    while c_queue or p_queue:

        if p_queue:
            node = p_queue.pop(0)
            for i in p[node]:
                if not visit[i]:
                    visit[i] = 1
                    p_queue.append(i)
        if c_queue:
            node = c_queue.pop(0)
            for i in c[node]:
                if not visit[i]:
                    visit[i] = 1
                    c_queue.append(i)


for t in range(1,T+1):
    N = int(input())
    M = int(input())
    p = [[] for _ in range(N+1)]
    c = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v = map(int,input().split())
        p[v].append(u)
        c[u].append(v)
    cnt = 0
    for i in range(1,N+1):
        visit = [0] * (N + 1)
        bfs(i)
        if sum(visit)==N:
            cnt+=1
    print("#{} {}".format(t,cnt))