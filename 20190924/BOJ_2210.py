
def back(tmp,k,x,y):
    global reuslt
    if k ==5:
        result.add(tmp)
        return
    else:
        if x-1>=0:
            back(tmp+board[x-1][y],k+1,x-1,y)
        if x+1 < 5:
            back(tmp + board[x + 1][y], k + 1, x + 1, y)
        if y-1>=0:
            back(tmp+board[x][y-1],k+1,x,y-1)
        if y+1 < 5:
            back(tmp + board[x][y+1], k + 1, x, y+1)

board = [''.join(input().split()) for _ in range(5)]

result = set()
for i in range(5):
    for j in range(5):
        back(board[i][j], 0, i, j)
print(result)
print(len(result))