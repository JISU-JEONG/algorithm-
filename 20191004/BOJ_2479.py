from collections import deque
import sys
input = sys.stdin.readline
def bfs(S):
    visit[S] = 1
    dq = deque()
    dq.append(S)
    while dq:
        q = dq.popleft()
        for v in G[q]:
            if not visit[v]:
                visit[v]=1
                P[v] = q
                dq.append(v)
                if v == E-1:
                    return 1
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
P = [0]*N
P[S-1] =S-1
r = bfs(S-1)
x = E-1
if r ==-1:
    print(-1)
else:
    result = []
    while P[x] != x:
        result.append(x)
        x = P[x]
    result.append(x)
    result.reverse()
    print(*map(lambda x:x+1,result))