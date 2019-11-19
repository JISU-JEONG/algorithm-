
def bfs(start):
    visit[start] = 1
    queue = [start]
    while queue:
        q = queue.pop(0)
        for i in person[q]:
            if not visit[i]:
                visit[i] = 1
                queue.append(i)

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    person = [[] for _ in range(N+1)]
    cnt = 0
    for _ in range(M):
        a,b = map(int,input().split())
        person[a].append(b)
        person[b].append(a)

    visit = [0]*(N+1)
    for i in range(1,N+1):
        if not visit[i]:
            bfs(i)
            cnt+=1

    print("#{} {}".format(t, cnt))