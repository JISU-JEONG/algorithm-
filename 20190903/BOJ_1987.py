
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def back(cnt, choice, x, y):
    global Max
    if Max == 26:
        return
    else:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] not in choice:
                    choice.append(board[nx][ny])
                    back(cnt+1, choice, nx, ny)
                    choice.pop()
                else:
                    Max = max(cnt, Max)
    return

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))
Max = 1
back(1,[board[0][0]],0,0)
print(Max)