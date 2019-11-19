
T = int(input())
for t in range(1,T+1):
    N,M,l = map(int,input().split())
    H = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
    h = 0
    for i in range(1,N):
        if 2*i<=N:L[i] = 2*i
        if 2*i+1<=N:R[i] = 2*i+1
    for i in range(M):
        a,b = map(int, input().split())
        H[a] = b
    for i in range(N,0,-1):
        if H[i]==0:
            H[i] = H[L[i]]+H[R[i]]
    print("#{} {}".format(t,H[l]))