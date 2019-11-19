def DFS(a, start, goal):
    visited = []
    queue = [start]

    while queue:
        p = queue.pop(0)
        if p == goal:
            return 1
        if p not in visited:
            visited.append(p)
            queue.extend(a[p])

    return 0


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    for _ in range(E):
        x, y = map(int, input().split())
        node[x].append(y)

    S, G = map(int, input().split())
    print('#{} {}'.format(test_case, DFS(node, S, G)))