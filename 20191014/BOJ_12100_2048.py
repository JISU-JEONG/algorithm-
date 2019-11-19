import copy
def back(k, board):
    global Max
    if k==5:
        Max = max(Max,max(map(max,board)))
        return
    else:
        new = copy.deepcopy(board)
        for i in range(4):
            next = move(new,i)
            back(k+1,next)
def move(board, d):
    new = [[0]*N for _ in range(N)]
    if d==0:
        for i in range(N):
            cmp, j, k = 0, 0, 0
            while j<N:
                if board[i][j]==0:
                    j+=1
                    continue
                elif cmp == board[i][j]:
                    new[i][k-1] = 2*cmp
                    cmp=0;
                else:
                    cmp = board[i][j]
                    new[i][k] = board[i][j]
                    k+=1
                j += 1
    elif d==1:
        for i in range(N):
            cmp, j, k = 0, N-1, N-1
            while j>=0:
                if board[i][j]==0:
                    j-=1
                    continue
                elif cmp == board[i][j]:
                    new[i][k+1] = 2*cmp
                    cmp=0
                else:
                    cmp = board[i][j]
                    new[i][k] = board[i][j]
                    k -= 1
                j -= 1
    elif d == 2:
        for i in range(N):
            cmp, j, k = 0, 0, 0
            while j < N:
                if board[j][i] == 0:
                    j += 1
                    continue
                elif cmp == board[j][i]:
                    new[k - 1][i] = 2 * cmp
                    cmp = 0;
                else:
                    cmp = board[j][i]
                    new[k][i] = board[j][i]
                    k += 1
                j += 1
    else:
        for i in range(N):
            cmp, j, k = 0, N-1, N-1
            while j>=0:
                if board[j][i]==0:
                    j-=1
                    continue
                elif cmp == board[j][i]:
                    new[k+1][i] = 2*cmp
                    cmp=0
                else:
                    cmp = board[j][i]
                    new[k][i] = board[j][i]
                    k -= 1
                j -= 1
    return new


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
Max = 0
back(0,board)
print(Max)