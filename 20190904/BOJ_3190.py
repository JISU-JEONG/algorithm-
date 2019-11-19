from collections import deque
# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]
right = {0:1,1:2,2:3,3:0}
left = {0:3,1:0,2:1,3:2}

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    r,c = map(int, input().split())
    board[r-1][c-1] = 1
L = int(input())
command = dict()
for _ in range(L):
    a, b = input().split()
    command[int(a)] = b

# 뱀의 방향은 초기에 오른쪽
snake = deque()
d = 1
x,y = 0,0
board[x][y] = 2
snake.append((x, y))
time = 0
while True:
    time += 1
    nx, ny = x+dx[d], y + dy[d]
    # # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if nx<0 or N<=nx or ny<0 or N<=ny:
        break
    if board[nx][ny] == 1:
        board[nx][ny] = 2
        snake.append((nx,ny))
    elif board[nx][ny] == 2:
        break
    else:
        board[nx][ny] = 2
        snake.append((nx,ny))
        a,b = snake.popleft()
        board[a][b] = 0
    x,y = nx, ny
    if command.get(time):
        if command[time] == 'L':
            d = left[d]
        else:
            d = right[d]
print(time)
# # 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
# #
# # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.

# # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# # 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
