def dfs():
    visited[1] = 1
    queue = [1]
    cnt = 0
    while queue:
        q = queue.pop(0)

        for num in com[q]:
            if visited[num] == 0:
                visited[num] = 1
                queue.append(num)
                cnt += 1
    return cnt

N = int(input())
M = int(input())
visited = [0]*(N+1)
com = [[] for _ in range(N+1)]
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

print(dfs())