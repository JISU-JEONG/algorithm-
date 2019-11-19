T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    p = list(range(N+1))
    ans = N
    def find_set(x):
        if x!=p[x]:
            p[x] = find_set(p[x])
        return p[x]
    pair = list(map(int,input().split()))
    for i in range(M):
        u,v = pair[2*i],pair[2*i+1]
        a,b = find_set(u),find_set(v)
        if a!=b:
            p[b] = a
            ans-=1
    print("#{} {}".format(t,ans))