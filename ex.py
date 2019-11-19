from itertools import combinations
from collections import deque

def bfs(c, z_num):
    global result, N
    time = 0
    queue = deque(c)
    for s in c: visited[s[0]][s[1]] = True
    while queue and z_num:
        time += 1
        len_queue = len(queue)  # 무조건 복사해야된다.
        for _ in range(len_queue):
            if not z_num: break
            y, x = queue.popleft()
            for nxt in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nxt_y, nxt_x = y + nxt[0], x + nxt[1]
                if (0 <= nxt_y < N and 0 <= nxt_x < N) and not visited[nxt_y][nxt_x]:
                    if virus_map[nxt_y][nxt_x] == 0:
                        visited[nxt_y][nxt_x] = True
                        queue.append((nxt_y, nxt_x))
                        z_num -= 1
                    elif virus_map[nxt_y][nxt_x] == 2:
                        visited[nxt_y][nxt_x] = True
                        queue.append((nxt_y, nxt_x))
    if z_num == 0:
        result = min(time, result)


N, M = map(int, input().split())
virus_map = []
virus_init_pos = []
zero_count = 0
result = float('inf')
for y in range(N):
    row = []
    for x, v in enumerate(map(int, input().split())):
        row.append(v)
        if v == 2:
            virus_init_pos.append((y, x))
        elif v == 0:
            zero_count += 1
    virus_map.append(row)
for c in combinations(virus_init_pos, M):
    visited = [[False] * N for _ in range(N)]
    bfs(list(c), zero_count)
print(-1) if result == float('inf') else print(result)