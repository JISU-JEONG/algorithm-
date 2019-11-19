

N, M = map(int,input().split())
castle = [list(input()) for _ in range(N)]
wave = [[0]*M for _ in range(N)]
p =[]


for i in range(N):
    for j in range(M):
        if castle[i][j] == '.':
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                nx, ny = i+dx, j+dy
                if 0<=nx<N and 0<=ny<M:
                    wave[nx][ny]+=1
        else:
            p.append((i,j))
while p:
    result = []
    for x,y in p:
        nx,ny