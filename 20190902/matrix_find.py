from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(start):
    visit[start[0]][start[1]] = 1
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx <N and 0<= ny <N:
                if not visit[nx][ny] and board[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx,ny))
                    end = (nx,ny)
    return end


T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    result = []
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and board[i][j]:
                start = (i, j)
                end = bfs(start)
                cnt += 1
                s1, s2 = end[0]-start[0]+1,end[1]-start[1]+1
                result.append((s1*s2,s1,s2))
    result.sort()
    print('#{} {} '.format(t,cnt),end='')
    for i in range(len(result)):
        if i == len(result)-1:
            print(result[i][1], result[i][2])
        else:
            print(result[i][1],result[i][2],end=' ')
