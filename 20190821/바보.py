import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
def dfs(x, y):
   visit[x][y] = 1
   print(x,  y)
   if x == 99:
       if board[x][]
          print(2)
       return True
   for i in [1, -1]:
       ty = y + i
       if 0<= ty < 100:
           if board[x][ty] == 1 and visit[x][ty] == 0:
               dfs(x, ty)
               break
   else:
        dfs(x + 1, y)

for _ in range(10):
   tc = input()
   board = []
   for _ in range(100):
       board.append(list(map(int, input().split())))
   for i in range(100):
       visit = [[0 for _ in range(100)] for _ in range(100)]
       result = []
       if board[0][i] == 1:
           print(dfs(0, i))