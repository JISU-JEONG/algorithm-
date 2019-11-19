def dfs(v):
    # 시작점을 방문하고, 스택에 push
    s =[]
    visit[v] = True; print(v, end=' ')
    s.append(v)
    # 빈스택이 아닐동안 반복
    while s:
        for w in G[v]:
            if not visit[w]:    # v의 방문하지 않은 인접정점 w에 찾아서
                visit[w]=True; print(w,end =' ')   # w를 방문하고, v를 스택에 push
                s.append(v)
                v = w
                break   # v를 w로 설정
        # 인접정점이 없다면, 스택에서 pop()해서
        else:
            v = s.pop() # v로 설정

V ,E = map(int,input().split()) #정점수, 간선수
G = [[] for _ in range(V+1)] # 1 ~ V 까지
visit = [False]*(V+1) # 방문정보
result = []

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V+1):
    print(i,'-->',G[i])

dfs(1)


# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
