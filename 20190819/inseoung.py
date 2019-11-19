import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = deque()
tmp1 = 0
count = 0
for m in range(M):
    for n in range(N):
        if tomato[n][m] == 1:
            q.append((m, n))
            tmp1 += 1
        elif tomato[n][m] == 0:
            count += 1
if not q:
    sys.stdout.write(0)
else:
    count = 0
    tmp2 = 0
    while q:
        m, n = q.popleft()
        tomato[n][m] = 1
        tmp1 -= 1
        tmp = 0

        for i in range(4):
            x1, y1 = n + dx[i], m + dy[i]
            if 0 <= x1 <M and 0 <= y1 < N and not tomato[y1][x1]:
                q.append((x1, y1))
                tmp += 1
        tmp2 += tmp
    sys.stdout.write(-1) if count else sys.stdout.write(count - 1)