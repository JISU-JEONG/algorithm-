


for _ in range(10):
    N, S = map(int, input().split())
    call = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    for i in range(N//2):
        G[call[2*i]].append(call[2*i+1])
    
