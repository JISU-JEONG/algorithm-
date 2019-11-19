from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0 , 0]
def limit(x,y):
    if 0<=x<1001 and 0<=y<1001: return 1
    else: return 0
def bfs(start):
    global cell_cnt

    for x,y in start:
        visit[x][y] = board[x][y]
    queue = deque(start)
    live = deque(start)
    time = 0
    while queue:
        time += 1
        newlive = deque()
        for x, y in queue:
            life[x][y] -= 1

        while live:
            x, y = live.popleft()
            dead[x][y] -= 1
            if dead[x][y] ==0:
                cell_cnt -= 1
            else:
                newlive.append((x,y))
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if life[x][y] ==0:
                for i in range(4):
                    nx, ny = x+ dx[i], y + dy[i]
                    if visit[nx][ny] < board[x][y] and life[nx][ny]==-1 or life[nx][ny] == board[nx][ny]+1:
                        if not visit[nx][ny]:
                            cell_cnt += 1
                            queue.append((nx, ny))
                            newlive.append((nx, ny))
                        visit[nx][ny] = board[x][y]
                        board[nx][ny] = board[x][y]
                        life[nx][ny] = board[x][y]+1
                        dead[nx][ny] = 2*board[x][y]
            else:
                queue.append((x,y))
        live = newlive
        if time == K: break


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [[0]*1001 for _ in range(1001)]
    visit = [[0] * 1001 for _ in range(1001)]
    life = [[-1] * 1001 for _ in range(1001)]
    dead = [[-1] * 1001 for _ in range(1001)]
    cell = [list(map(int, input().split())) for _ in range(N)]
    cell_cnt = 0
    start = []
    for i in range(N):
        for j in range(M):
            if cell[i][j]:
                board[500+i][500+j] = cell[i][j]
                life[500 + i][500 + j] = cell[i][j]+1
                dead[500 + i][500 + j] = 2*cell[i][j]
                cell_cnt += 1
                start.append((500+i,500+j))

    bfs(start)
    print('#{} {}'.format(t,cell_cnt))
