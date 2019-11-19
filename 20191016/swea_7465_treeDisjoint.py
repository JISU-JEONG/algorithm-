import sys


T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    p= list(range(N+1)) # 1~N. make-set(모든정점)
    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x]) # path-compression
        return p[x]

    ans = N
    for _ in range(M):
        u, v = map(int,input().split())
        a = find_set(u); b = find_set(v)
        if a!=b:
            p[b] = a
            ans -= 1

    print("#{} {}".format(t, ans))