import sys
sys.setrecursionlimit(10**6)
def omok(x,y,cnt,h):
    s = 0
    if 0<=x<19 and 0<=y<19 and omok[x][y]==h:
        s += omok(x, y + 1, cnt + 1, h)
        s += omok(x+1, y, cnt + 1, h)
        s += omok(x+1, y + 1, cnt + 1, h)

        if s > 0: return 1
        else: return 0

    else:
        if cnt == 5:
            return 1
        else:
            return 0


board = [list(input().split()) for _ in range(19)]
pos = (0, 0)
for i in range(19):
    for j in range(19):
        if board[i][j]:
            print(omok(i, j, 0, board[i][j]))
