from collections import deque
import copy
import pprint

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def back(choice, k):

    global Max

    if len(choice) ==3:
        clab = copy.deepcopy(lab)
        cnt = safty_cnt-3
        for x,y in choice:
            clab[x][y] = 1
        visit = [[0]*M for _ in range(N)]

        Max = max(Max, bfs(cnt,visit,clab))
        return
    else:
        for i in range(k,len(wall)):
            if not used[i]:
                used[i] = 1
                choice.append(wall[i])
                back(choice,i+1)
                used[i] = 0
                choice.pop()

def bfs(cnt, visit,clab):
    queue = deque()
    for i,j in virus:
        visit[i][j] = 1
        queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<= ny < M:
                if not visit[nx][ny] and not clab[nx][ny]:
                    cnt -=1
                    visit[nx][ny] = 1
                    clab[nx][ny] = 2
                    queue.append((nx,ny))
    return cnt


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
wall = deque()
virus = deque()
Max = 0
safty_cnt = 0
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i,j))
        elif lab[i][j] == 0:
            wall.append((i,j))
            safty_cnt += 1
used = [0]*len(wall)
back([], 0)

print(Max)