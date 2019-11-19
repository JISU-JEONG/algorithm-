from queue import PriorityQueue


T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    D = [[0xffff]*N for _ in range(N)]
    Q = PriorityQueue()
    Q.put((0,0,0))
    D[0][0] =0
    while not Q.empty():
        d,x,y = Q.get()
        if D[x][y] < d: continue
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                w = max(0,board[nx][ny]-board[x][y])+1
                if D[nx][ny] > D[x][y]+w:
                    D[nx][ny] = D[x][y]+w
                    Q.put((D[nx][ny],nx,ny))
    print("#{} {}".format(t,D[N-1][N-1]))
