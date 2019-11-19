def bfs(start):
    queue =[start]
    visited = [start]

    while queue:
        p = queue.pop()

        for i in node[p]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

    return len(visited)-1


N = int(input())
pair= int(input())

node = [[] for x in range(N+1)]

for i in range(pair):
    f, s = map(int, input().split())
    node[f].append(s)
    node[s].append(f)

result = bfs(1)
print(result)