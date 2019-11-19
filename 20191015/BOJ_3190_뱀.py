import pprint
import collections

# 방향 d = 0,1,2,3 상하좌우
L = {0:2, 2:1,1:3,3:0}
R = {2:0,0:3,3:1,1:2}
dx = [-1,1,0,0]
dy = [0,0,-1,1]
N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    x,y =map(int,input().split())
    board[x-1][y-1] = 2
command = dict()
T = int(input())
for _ in range(T):
    num, c = input().split()
    command[int(num)] = c
snake = collections.deque()
snake.append((0,0))
board[0][0] = 1
time = 0
d = 3
while True:
    time+=1
    nx, ny = snake[-1][0]+dx[d], snake[-1][1]+dy[d]
    if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny]==1:
        break
    snake.append((nx,ny))
    if board[nx][ny] != 2:
        x,y = snake.popleft()
        board[x][y] = 0
    board[nx][ny] = 1
    if command.get(time):
        if command[time] =='L':
            d =L[d]
        else:
            d =R[d]
print(time)