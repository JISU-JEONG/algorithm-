import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def reroll(c):

    if c == 1:
        dice[0][1], dice[1][2], dice[2][1], dice[1][0] = dice[1][0], dice[0][1], dice[1][2], dice[2][1]
    elif c == 2:
        dice[0][1], dice[1][2], dice[2][1], dice[1][0] = dice[1][2], dice[2][1], dice[1][0], dice[0][1]
    elif c == 3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    else:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]

N, M, x, y, K = map(int, input().split())
dice = [
    ['', 0, ''],
    [ 0, 0, 0],
    ['', 0, ''],
    ['', 0, '']
]

board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다.
# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
for c in command:
    nx, ny = x + dx[c-1], y+dy[c-1]
    if 0<=nx <N and 0<=ny<M:
        reroll(c)
        if board[nx][ny] ==0:
            board[nx][ny] = dice[2][1]
        else:
            dice[2][1] = board[nx][ny]
            board[nx][ny] = 0
        x,y = nx,ny
        print(dice[0][1])
# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면,
# 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며,
# 칸에 쓰여 있는 수는 0이 된다.

# 주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

# 주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.