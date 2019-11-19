def check(x, y, dx, dy):
    nx, ny = x, y
    while True:
        nx += dx
        ny += dy
        if 0<=nx<N and 0<= ny<N:
            if data[nx][ny] != 0:
                if data[nx][ny] != data[x][y]:
                    return
                elif data[nx][ny] == data[x][y] and change[nx][ny] == 0:
                    data[nx][ny] += data[x][y]
                    change[nx][ny] = 1
                    data[x][y] = 0
                    return
            else:
                continue
        else:
            return


def move(x, y, dx, dy):
    nx, ny = x, y
    value = data[x][y]
    count = 0
    while True:
        nx += dx
        ny += dy
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == 0:
                count += 1
            else:
                break
        else:
            break
    if count > 0:
        data[x+dx*count][y+dy*count] = value
        data[x][y] = 0
    return

T = int(input())
for t in range(T):
    N, S = input().split()
    N = int(N)
    data = []
    change = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(N):
        data.append(list(map(int, input().split())))

    if S == 'up':
        for i in range(1, N):
            for j in range(N):
                if data[i][j] == 0:
                    continue
                else:
                    check(i,j,-1,0)
        for i in range(1, N):
            for j in range(N):
                if data[i][j] == 0:
                    continue
                else:
                    move(i,j,-1,0)

    elif S == 'down':
        for i in range(N-2, -1, -1 ):
            for j in range(N):
                if data[i][j] == 0:
                    continue
                else:
                    check(i,j,1,0)
        for i in range(N-2, -1, -1 ):
            for j in range(N):
                if data[i][j] == 0:
                    continue
                else:
                    move(i,j,1,0)
    elif S == 'left':
        for i in range(N):
            for j in range(1, N):
                if data[i][j] == 0:
                    continue
                else:
                    check(i,j,0,-1)
        for i in range(N):
            for j in range(1, N):
                if data[i][j] == 0:
                    continue
                else:
                    move(i,j,0,-1)
    elif S == 'right':
        for i in range(N):
            for j in range(N-2, -1, -1):
                if data[i][j] == 0:
                    continue
                else:
                    check(i,j,0,1)
        for i in range(N):
            for j in range(N-2, -1, -1):
                if data[i][j] == 0:
                    continue
                else:
                    move(i,j,0,1)
    print('#{}'.format(t+1))
    for d in data:
        for a in d:
            print(a, end=' ')
        print()