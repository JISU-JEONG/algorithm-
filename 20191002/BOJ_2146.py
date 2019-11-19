from collections import deque
import sys

input = sys.stdin.readline


def find(sx, sy):
    stack.append((sx, sy))
    visit[sx][sy] = 1
    dq = deque()
    dq.append((sx, sy))
    while dq:
        x, y = dq.popleft()
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visit[nx][ny] and land[nx][ny]:
                    visit[nx][ny] = 1
                    dq.append((nx, ny))
                    stack.append((nx, ny))


N = int(input())

land = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
L = 0xffff
result = []
for i in range(N):
    for j in range(N):
        if not visit[i][j] and land[i][j]:
            stack = []
            find(i, j)
            result.append(stack)
for r in result:
    print(r)
for i in range(len(result) - 1):
    for j in range(i + 1, len(result)):
        for x1, y1 in result[i]:
            for x2, y2 in result[j]:
                L = min(L, abs(x1 - x2) + abs(y1 - y2))
print(L - 1)
