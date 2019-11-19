dx = [0, 0, -1]
dy = [-1, 1, 0]

def limit(x,y):
    if 0 <= x < 100 and 0 <= y < 100: return 1
    else: return 0

def dfs(x, y):
    global find
    visit[x][y] = True
    if x == 0:
        find = y
        return
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if limit(nx,ny) and not visit[nx][ny] and ladder[nx][ny]:
            dfs(nx, ny)
            break

for _ in range(10):
    t = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    start = (0,0)
    find = 0
    for i in range(100):
        if ladder[99][i] == 2:
            start=(99, i)
            break
    visit = [[0]*100 for _ in range(100)]
    dfs(start[0], start[1])
    print('#{} {}'.format(t, find))