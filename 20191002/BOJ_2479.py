
def dfs(S):
    visit[S] = 1
    result.append(S)
    if S == E-1:
        return result
    for v in G[S]:
        if not visit[v]:
            return dfs(v)
    return -1

N,M = map(int, input().split())
Min = N+1
bin = [list(input()) for _ in range(N)]
G = [[] for _ in range(N)]
visit = [0]*N
for i in range(N-1):
    for j in range(i+1,N):
        cnt = 0
        for k in range(M):
            if bin[i][k] != bin[j][k]:
                cnt+=1
                if cnt>1:
                    break
        if cnt==1:
            G[i].append(j)
            G[j].append(i)
S, E = map(int, input().split())
result = []
dfs(S-1)
if len(result)==1:
    print(-1)
else:
    print(*map(lambda x:x+1, result))