
def dfs(x):
    visit[x] += 1
    result.append(x)
    for w in G[x]:
        visit[w] += 1
        if visit[w] == d[w]:
            dfs(w)

for t in range(1, 11):
    V, E = map(int, input().split())
    line = list(map(int, input().split()))
    G = [[] for _ in range(V+1)]
    visit = [0]*(V+1)
    d = [0] * (V+1)
    result = []
    for i in range(0, E):
        G[line[2*i]].append(line[2*i+1])
        d[line[2*i+1]] += 1

    for i in range(1, V+1):
        if d[i] == 0:
            dfs(i)

    print('#'+str(t),*result)
