import pprint
# 0 1 2 3 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solution(rx,ry,bx,by,d):

    nrx, nry, nbx, nby = rx,ry,bx,by
    while board[nrx][nry] !='#' and board[nrx][nry] !='O':
        nrx, nry = nrx+dx[d], nry+dy[d]
    if board[nrx][nry] =='#':
        nrx, nry = nrx - dx[d], nry - dy[d]
    board[rx][ry] = '.'
    while board[nbx][nby] !='#' and board[nbx][nby] !='O':
        nbx, nby = nbx+dx[d], nby+dy[d]
    if board[nbx][nby] =='#':
        nbx, nby = nbx - dx[d], nby - dy[d]
    board[bx][by] = '.'
    if nrx ==nbx and nry ==nby and board[nbx][nby] !='O':
        if abs(rx-nrx)+abs(ry-nry) > abs(bx-nbx)+abs(by-nby):
            nrx, nry = nrx - dx[d], nry - dy[d]
        else:
            nbx, nby = nbx - dx[d], nby - dy[d]
    return nrx, nry, nbx, nby

from collections import deque
def bfs(rx,ry,bx,by):
    visit[rx][ry][bx][by] = 1
    queue = deque()
    queue.append((rx,ry,bx,by))
    time = 0
    flag = 0
    while queue:
        if flag == 1: break
        time+=1
        for _ in range(len(queue)):
            if flag ==1: break
            rx,ry,bx,by = queue.popleft()
            for i in range(4):
                nrx, nry, nbx, nby = solution(rx,ry,bx,by,i)
                if nrx == nbx and nry == nby:
                    continue
                elif nrx == ox and nry == oy:
                    flag =1
                    break
                elif nbx == ox and nby == oy:
                    continue
                elif not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] =1
                    queue.append((nrx,nry,nbx,nby))
        if time == 10:
            break
    if flag == 1:
        return time
    else:
        return -1

N, M =map(int, input().split())
board = [list(input()) for _ in range(N)]
visit = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry =i, j
        if board[i][j] == 'B':
            bx,by = i, j
        if board[i][j] == 'O':
            ox,oy = i, j

result = bfs(rx,ry,bx,by)
print(result)