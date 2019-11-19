
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def back(cnt, s , x, y):
    global Max
    if cnt ==4:
        Max = max(s,Max)
    else:
        stack = []
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    back(cnt+1,s+board[nx][ny],nx,ny)
                    visit[nx][ny] = 0
                    stack.append(i)
        if len(stack) >=2 and cnt ==2:
            for i in range(len(stack)-1):
                for j in range(i+1,len(stack)):
                    nx1, ny1 = x + dx[stack[i]], y + dy[stack[i]]
                    nx2, ny2 = x + dx[stack[j]], y + dy[stack[j]]
                    visit[nx1][ny1]=1; visit[nx2][ny2]=1
                    back(cnt+2,s+board[nx1][ny1]+board[nx2][ny2],x,y)
                    visit[nx1][ny1] = 0;visit[nx2][ny2] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
Max = 0
for i in range(N):
    for j in range(M):
        visit[i][j] =1
        back(1,board[i][j],i,j)
        visit[i][j] = 0
print(Max)