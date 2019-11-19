from collections import deque

def bfs(start):
    visit[start] = 1
    queue = deque([start])
    result = []
    temp = []
    while queue:
        for i in range(len(queue)):
            q = queue.popleft()
            for w in G[q]:
                if not visit[w]:
                    visit[w] = 1
                    queue.append(w)
                    result.append(w)
        if result:
            temp = result.copy()
            result = []

    return temp

for t in range(1, 11):
    L , start = map(int, input().split())
    tel = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    visit =[0]*101
    for i in range(L//2):
        G[tel[2*i]].append(tel[2*i+1])

    result = bfs(start)
    print('#{} {}'.format(t,max(result)))