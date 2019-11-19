dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]


def bfs(sx,sy):
    visit[sx][sy] =1
    queue = [(sx,sy)]
    time = -1
    while queue:
        time += 1
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            if x==endx and y == endy:
                return time
            for i in range(8):
                nx, ny = x+dx[i], y + dy[i]
                if 0<=nx<N and 0<= ny<N:
                    if not visit[nx][ny]:
                        visit[nx][ny] = 1
                        queue.append((nx,ny))

T = int(input())

for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    endx, endy = map(int, input().split())
    visit = [[0] * N for _ in range(N)]
    result = bfs(sx,sy)
    print(result)