import sys

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def solution(T, check):

    k =0

    while k < T:
        k += 1
        # 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
        plus = [[0]*C for _ in range(R)]
        for x, y in check:
            # 얼마나 나누어 주었나 카운트
            cnt = 0
            # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
            # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                # 범위 밖이 아니고 공기 청정기 위치도 아니면
                if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                    # 확산되는 양은 Ar,c/5이고 소수점은 버린다.
                    plus[nx][ny] += room[x][y]//5
                    cnt += 1

            # (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
            plus[x][y] -= (room[x][y]//5)*cnt
        # 공기청정기가 작동한다.
        # 공기청정기에서는 바람이 나온다.

        for i in range(R):
            for j in range(C):
                room[i][j] += plus[i][j]

        tmp1, tmp2 = 0, 0
        # 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
        # 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
        # 위쪽


        for i in range(1,C):
            tmp1, room[robot[0]][i] = room[robot[0]][i], tmp1
            tmp2, room[robot[1]][i] = room[robot[1]][i], tmp2
        for i in range(robot[0]-1,-1,-1):
            tmp1, room[i][C-1] = room[i][C-1], tmp1
        for i in range(robot[1]+1,R):
            tmp2, room[i][C-1] = room[i][C-1], tmp2
        for i in range(C-2,-1,-1):
            tmp1, room[0][i] = room[0][i], tmp1
            tmp2, room[R - 1][i] = room[R - 1][i], tmp2
        for i in range(1, robot[0]-1):
             tmp1, room[i][0] = room[i][0], tmp1
        for i in range(R-2, robot[1],-1):
            tmp2, room[i][0] = room[i][0], tmp2


       # 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

        check = []
        for i in range(R):
            for j in range(C):
                if room[i][j] >= 5:
                    check.append((i,j))


R, C, T = map(int, sys.stdin.readline() .split())

room = [list(map(int, sys.stdin.readline() .split())) for _ in range(R)]
check = []
robot= []
for i in range(R):
    for j in range(C):
        if room[i][j] != 0 and room[i][j] != -1:
            check.append((i,j))
        elif room[i][j] == -1:
            robot.append(i)

solution(T, check)

print(sum(map(sum,room))+2)

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
s1, s2 = -1, 0

def diffuse():
    global a
    b = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j] >= 5:
                d = a[i][j]//5
                for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < r and 0 <= nj < c and a[ni][nj] != -1:
                        b[ni][nj] += d
                        a[i][j] -= d
    for i in range(r):
        for j in range(c):
            a[i][j] += b[i][j]

def purify():
    for i in range(s1-2, -1, -1):
        a[i+1][0] = a[i][0]
    for i in range(c-1):
        a[0][i] = a[0][i+1]
    for i in range(s1):
        a[i][c-1] = a[i+1][c-1]
    for i in range(c-2, -1, -1):
        a[s1][i+1] = a[s1][i]
    a[s1][1] = 0
    for i in range(s2+1, r-1):
        a[i][0] = a[i+1][0]
    for i in range(c-1):
        a[r-1][i] = a[r-1][i+1]
    for i in range(r-2, s2-1, -1):
        a[i+1][c-1] = a[i][c-1]
    for i in range(c-2, -1, -1):
        a[s2][i+1] = a[s2][i]
    a[s2][1] = 0

def solve():
    for _ in range(t):
        diffuse()
        purify()
    print(sum(map(sum, a))+2)

for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            if s1 == -1:
                s1 = i
            else:
                s2 = i
solve()
