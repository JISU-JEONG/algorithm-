import sys
from collections import deque
input = sys.stdin.readline
def bfs(s):
    visit[s] = 1
    check[s] = 1
    queue = deque()
    queue.append(s)
    cnt = 1
    while queue:
        q = queue.popleft()
        for v in G[q]:
            if not visit[v]:
                visit[v]=1
                cnt+=1
                queue.append(v)
                check[s] =1
    return cnt

N, M =map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    G[b].append(a)
Max = 0
result = []
check = [0]*(N+1)
for i in range(1,N+1):
    if not check[i]:
        visit = [0] * (N + 1)
        r =bfs(i)
        if Max< r:
            Max = r
            result=[i]
        elif Max == r:
            result.append(i)

print(*result)