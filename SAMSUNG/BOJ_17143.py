# 1 위 2 아래 3 오른쪽 4 왼쪽
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
reflect = {1:2,2:1,3:4,4:3}
R, C, M = map(int, input().split())
shark = dict()
sea = [[0]*(C+1) for _ in range(R+1)]
fishing = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[(r, c)] = [s, d, z]
    sea[r][c] = 1

for i in range(1,C+1):
    # 가장 가까운 상어를 찾는다.
    for j in range(1,R+1):
        if sea[j][i]:
            fishing += shark[(j,i)][2]
            del shark[(j,i)]
            sea[j][i] = 0
            break

    new_shark = dict()
    for key, value in shark.items():
        x,y = key
        sea[x][y] = 0
        s, d, z = value
        nx, ny = x+dx[d]*s, y+dy[d]*s
        while nx<1 or R<nx or ny<1 or C<ny:
            d = reflect[d]
            if nx<1:
                nx = 2-nx
            elif nx>R:
                nx = 2*R - nx
            elif ny <1:
                ny = 2-ny
            elif ny >C:
                ny = 2*C - ny
        if new_shark.get((nx,ny)):
            if new_shark[(nx,ny)][2] < z:
                new_shark[(nx,ny)][0] = s
                new_shark[(nx,ny)][1] = d
                new_shark[(nx,ny)][2] = z
        else:
            new_shark[(nx,ny)] = [s,d,z]
    for x,y in new_shark:
        sea[x][y] = 1
    shark = new_shark

print(fishing)