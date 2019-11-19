dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs():
    global shark_eat, fish_count, shark_size
    start = [(shark_x, shark_y)]
    queue =[]
    times = 0

    while start:
        p = start.pop()
        visitied = [[0]*N for _ in range(N)]
        visitied[p[0]][p[1]] = 1
        size = 1
        queue.append(p)
        if fish_count == 0:
            break
        while queue:
            for _ in range(size):
                q = queue.pop(0)
                for i in range(4):
                    nx = q[0] + dx[i]
                    ny = q[1] + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and visitied[nx][ny] == 0 and (sea[nx][ny] == shark_size or sea[nx][ny] == 0):
                        queue.append((nx, ny))
                        visitied[nx][ny] = visitied[q[0]][q[1]]+1
                    elif 0 <=nx < N and 0 <= ny < N and sea[nx][ny] != 0 and shark_size > sea[nx][ny] and visitied[nx][ny] == 0:
                        start.append((nx, ny))
                        visitied[nx][ny] = visitied[q[0]][q[1]] + 1
            if len(start):
                sx, sy = start[0][0], start[0][1]
                for x, y in start:
                    if x < sx:
                        sx = x
                        sy = y
                    elif x == sx and y < sy:
                        sx = x
                        sy = y
                shark_eat += 1
                if shark_eat == shark_size:
                    shark_size += 1
                    shark_eat = 0
                sea[p[0]][p[1]] = 0
                sea[sx][sy] = 9
                queue = []
                fish_count -= 1
                times += visitied[sx][sy]-1
                start = [(sx,sy)]
                break
            size = len(queue)

    return times


N = int(input())

sea = [list(map(int, input().split())) for _ in range(N)]
shark_x = shark_y = 0
fish_count = 0
fish_cnt =[]
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_x, shark_y = i, j
        elif sea[i][j] != 0:
            fish_count += 1

shark_size = 2
shark_eat = 0

result = bfs()
print(result)

