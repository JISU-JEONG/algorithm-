import sys
I = sys.stdin.readline
sys.setrecursionlimit(10**6)
def move(tx, ty, x, y):
   global cnt
   if x == N - 1 and y == N - 1:
       cnt += 1
       return
   else:
       ti, tj = x - tx, y - ty
       if ti + tj == 1:
           if x < N and y < N and board[x][y] == 0:
               move(x, y, x + ti, y + tj)
               move(x, y, x + 1, y + 1)
       else:
           if x < N and y < N and board[x - 1][y] == 0 and board[x][y - 1] == 0 and board[x][y] == 0:
               move(x, y, x + 1, y)
               move(x, y, x, y + 1)
               move(x, y, x + 1, y + 1)
N = int(I())
board =[]
cnt = 0
for _ in range(N):
   board.append(list(map(int, I().split())))
move(0, 0, 0, 1)
print(cnt)