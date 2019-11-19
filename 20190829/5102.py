
def bfs(start):
    visit[start] = 1
    queue = [start]
    while queue:
        q = queue.pop(0)
        for w in G[q]:
            if not visit[w]:
                visit[w] = visit[q]+1
                queue.append(w)

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    visit = [0]*(N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    start, end = map(int, input().split())
    if start == end:
        result = 0
    else:
        bfs(start)
        result = visit[end]-1
    if result <0: result = 0
    print('#{} {}'.format(t, result))