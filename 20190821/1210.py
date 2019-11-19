
dx = [0, 0, 1]
dy = [-1, 1, 0]

def limit(x,y):
    if 0 <= x < 100 and 0 <= y < 100:
        return 1
    else:
        return 0

def dfs(x, y):
    global find
    visit[x][y] = True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if limit(nx,ny) and not visit[nx][ny] and ladder[nx][ny]:
            if ladder[nx][ny] == 2:
                find =1
                return
            dfs(nx, ny)
            break

for _ in range(10):
    t = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    start = []
    find = 0
    for i in range(100):
        if ladder[0][i] == 1:
            start.append(i)

    for s in start:
        visit = [[False] * 100 for _ in range(100)]
        dfs(0, s)
        if find:
            print('#{} {}'.format(t,s))
            break


