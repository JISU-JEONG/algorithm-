from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(sx, sy):
    visit[sx][sy] = 1
    queue = deque()
    queue.append((sx, sy))
    time = 0
    while queue:
        time += 1
        for i in range(len(fire)):
            fx, fy = fire.popleft()
            for i in range(4):
                nfx, nfy = fx + dx[i], fy + dy[i]
                if 0<= nfx < h and  0<= nfy < w:
                    if not fire_visit[nfx][nfy] and board[nfx][nfy] != '#':
                        fire_visit[nfx][nfy] = 1
                        board[nfx][nfy] = '*'
                        fire.append((nfx,nfy))

        for i in range(len(queue)):
            x, y = queue.popleft()
            if x ==0 or y ==0 or x == h-1 or y == w-1:
                return time
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<= nx < h and  0<= ny < w:
                    if not fire_visit[nx][ny] and not visit[nx][ny] and board[nx][ny] == '.':
                        visit[nx][ny] = 1
                        board[nx][ny] = '@'
                        queue.append((nx,ny))
    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    fire_visit = [[0]*w for _ in range(h)]
    fire = deque()
    sx, sy = 0, 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire.append((i, j))
                fire_visit[i][j] = 1
            elif board[i][j] == '@':
                sx, sy = i, j
    result = bfs(sx, sy)
    print(result)