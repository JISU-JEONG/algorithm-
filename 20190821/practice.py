from collections import deque


def bfs(start):
    visitied[start] = 1
    result.append(start)
    queue = deque([start])

    while queue:
        q = queue.popleft()
        temp = []
        for node in board[q]:
            if visitied[node] == 0:
                temp.append(node)
                result.append(node)
                visitied[node] = 1
        queue.extendleft(temp)


def dfs(start):
    visitied[start] = 1
    queue = [start]
    result2.append(start)
    while queue:
        q = queue.pop(0)
        for node in board[q]:
            if visitied[node] == 0:
                queue.append(node)
                result2.append(node)
                visitied[node] = 1


N, M, V = map(int, input().split())
visitied = [0]*(N+1)
result = []
result2 = []
board = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

for i in range(N+1):
    board[i].sort()


bfs(V)
visitied = [0] * (N + 1)
dfs(V)
print(*result)
print(*result2)