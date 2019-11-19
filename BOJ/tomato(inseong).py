import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
​
q = deque()
tmp1 = 0
for m in range(M):
    for n in range(N):
        if tomato[n][m] == 1:
            q.append((m, n))
            tmp1 += 1
if not q:
    print(0)
else:
    count = 0
    tmp2 = 0
    flag = True
    while q:
        m, n = q.popleft()
        tomato[n][m] = 1
        tmp1 -= 1
        if m + 1 < M:
            if not tomato[n][m + 1]:
                q.append((m + 1, n))
                tmp2 += 1
        if 0 <= m - 1:
            if not tomato[n][m - 1]:
                q.append((m - 1, n))
                tmp2 += 1
        if n + 1 < N:
            if not tomato[n + 1][m]:
                q.append((m, n + 1))
                tmp2 += 1
        if 0 <= n - 1:
            if not tomato[n - 1][m]:
                q.append((m, n - 1))
                tmp2 += 1
        if tmp1 == 0:
            tmp1, tmp2 = tmp2, tmp1
            count += 1
    for n in range(N):
        if 0 in tomato[n]:
            flag = False
            break
    print(count-1) if flag else print(-1)