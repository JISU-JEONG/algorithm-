
def bfs(s):
    visit[s] = 1
    queue = [s]
    while queue:
        q = queue.pop(0)
        if q ==E:
            return visit[q]
        for v in G[q]:
            if not visit[v]:
                visit[v] = visit[q]+1
                queue.append(v)
    return 0

T = int(input())
S,E =map(int, input().split())
N = int(input())
G = [[] for _ in range(101)]
visit = [0]*101
for _ in range(N):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

print(bfs(S)-1)