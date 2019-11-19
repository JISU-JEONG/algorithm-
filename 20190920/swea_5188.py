
def back(x,y,s):
    global Min
    if s >= Min:
        return
    if x==N-1 and y ==N-1:
        Min = min(Min,s)

    else:
        if x+1 <N:
            back(x+1, y, s + board[x+1][y])
        if y+1 <N:
            back(x, y+1, s + board[x][y+1])

T = int(input())

for t in range(1, T+1):
    N = int(input())
    Min = 0xffff
    board = [list(map(int,input().split())) for _ in range(N)]
    back(0 , 0, board[0][0])
    print("#{} {}".format(t,Min))
