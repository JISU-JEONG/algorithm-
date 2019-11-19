import collections
import pprint

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visit = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
rx,ry,bx,by,endx,endy =0,0,0,0,0,0

for i in range(N):
    for j in range(M):
        if board[i][j]=='B':
            bx,by=i,j
        if board[i][j]=='R':
            rx,ry =i,j
        if board[i][j]=='O':
            endx,endy =i,j

visit[rx][ry][bx][by] = 1
dq = collections.deque()
dq.append((rx,ry,bx,by))
time = 0
flag = 0
while time < 11:
    time += 1
    for _ in range(len(dq)):
        q = dq.popleft()
        for dx,dy in (0,1),(0,-1),(-1,0),(1,0):
            nrx,nry,nbx,nby = q
            # 빨간 구슬 이동
            while True:
                nrx += dx;nry += dy
                if board[nrx][nry] =='#':
                    nrx-=dx; nry-=dy
                    break
                if board[nrx][nry] =='O':
                    break
            # 파란 구슬 이동
            while True:
                nbx += dx;nby += dy
                if board[nbx][nby] =='#':
                    nbx-=dx; nby-=dy
                    break
                if board[nbx][nby] =='O':
                    break
            if nbx==endx and nby == endy:
                continue
            if nrx==nbx and nby==nry:
                if abs(q[0]-nrx) > abs(q[2]-nbx) or abs(q[1]-nry) > abs(q[3]-nby):
                    nrx -=dx;nry-=dy
                else:
                    nbx -= dx;
                    nby -= dy
            if nrx==endx and nry == endy:
                flag = 1
                break
            elif nbx==endx and nby == endy:
                continue
            elif not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = 1
                dq.append((nrx,nry,nbx,nby))
        if flag ==1:
            break
    if flag == 1:
        break
time = -1 if time >10 else time
print(time)

