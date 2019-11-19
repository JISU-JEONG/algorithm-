


def bfs(s):
    visit[s] = 1
    queue = [s]
    cnt = 0
    while queue:
        cnt+=1
        for _ in range(len(queue)):
            q = queue.pop(0)
            for v in G[q]:
                if not visit[v]:
                    visit[v] = 1
                    queue.append(v)
    return cnt


N = int(input())
G = [[] for _ in range(N+1)]
while True:
    i,j=map(int,input().split())
    if i <0 and j<0:
        break
    G[i].append(j)
    G[j].append(i)
Min = 0xffff
ans = []
for i in range(1, N+1):
    visit = [0]*(N+1)
    result = bfs(i)
    if Min > result:
        ans = [i]
        Min = result
    elif Min==result:
        ans.append(i)
print(Min-1,len(ans))
print(*ans)