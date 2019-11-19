import pprint
# # # 로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
left = {0:3, 1:0, 2:1, 3:2}
back = {0:2, 1:3,3:1,2:0}
duty = 0
clean = 0
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            duty += 1

while True:
    # # # 현재 위치를 청소한다.
    if duty-clean == 0:
        break
    if board[r][c] == 0:
        board[r][c] = 2
        clean += 1
    # # # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    for i in range(4):
        nx, ny = r+dx[left[d]], c + dy[left[d]]
        # # # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        if not board[nx][ny]:
            d = left[d]
            r,c = nx, ny
            break
        else:
            # # # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
            d = left[d]
    # # # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    else:
        nx, ny = r+dx[back[d]], c + dy[back[d]]
        # # # 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        if board[nx][ny] == 1:
            break
        else:
            r, c = nx, ny
        # # # 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

print(clean)