
def bfs(i,j,k):
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    queue = [(i,j)]
    visit[i][j] = 1
    if home[i][j]:
        cnt+=1
    for i in range(k-1):
        for _ in range(len(queue)):
            x,y = queue.pop(0)
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                nx,ny = x+dx,y+dy
                if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    queue.append((nx,ny))
                    if home[nx][ny]:
                        cnt += 1
    return cnt
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    home = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if home[i][j]==1:
                cnt+=1
    k = 1
    while 2*k*(k-1)+1<=cnt*M:
        k+=1
    k-=1
    while k:
        Max = 0
        for i in range(N):
            for j in range(N):
                Max=max(Max,bfs(i,j,k))
        if 2*k*(k-1)+1<=Max*M: break
        k-=1
    print("#{} {}".format(t,Max))
