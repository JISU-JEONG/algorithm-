import pprint

def clean():
    tmp = 0
    for i in range(1,C):
        room[N-1][i],tmp = tmp, room[N-1][i]
    for i in range(N-2,-1,-1):
        room[i][C-1],tmp = tmp, room[i][C-1]
    for i in range(C-2,-1,-1):
        room[0][i],tmp = tmp,room[0][i]
    for i in range(1,N-1):
        room[i][0],tmp = tmp,room[i][0]
    tmp = 0
    for i in range(1,C):
        room[N][i],tmp = tmp, room[N][i]
    for i in range(N+1,R):
        room[i][C-1],tmp = tmp, room[i][C-1]
    for i in range(C-2,-1,-1):
        room[R-1][i],tmp = tmp,room[R-1][i]
    for i in range(R-2,N,-1):
        room[i][0],tmp = tmp,room[i][0]

from collections import deque
# 1초 동안 아래 적힌 일이 순서대로 일어난다.
dx = [0,0,1,-1]
dy = [1,-1,0,0]

R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]

N = 0

dust = deque()

for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            N = i
time = 0
while time < T:
    time += 1
    tmp = [[0]*C for _ in range(R)]
    # 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    for x in range(R):
        for y in range(C):
            if room[x][y] > 4:
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if 0<=nx<R and 0<=ny <C:
                        if room[nx][ny] != -1:
                            tmp[nx][ny] += room[x][y]//5
                            tmp[x][y] -= room[x][y]//5
    # 확산되는 양은 Ar,c/5이고 소수점은 버린다.
    # (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
    for i in range(R):
        for j in range(C):
            room[i][j] += tmp[i][j]
    # 공기청정기가 작동한다.
    # 공기청정기에서는 바람이 나온다.
    # 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    clean()
    # 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    # 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.


print(sum(map(sum, room))+2)
