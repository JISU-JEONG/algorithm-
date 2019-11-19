
def solution(k):
    global flag
    if flag == 1:
        return
    if k == L:
        flag = 1
        for i in range(len(board)):
            print(*board[i])
        return
    else:
        for i in range(L):
            if used[i] == 0:
                x, y = result[i]
                used[i] = 1
                q = find(x,y)
                if not q:
                    used[i] = 0
                    return
                for j in q:
                    board[x][y] =j
                    solution(k+1)
                used[i] = 0
                board[x][y] = 0

def find(x, y):
    result = set()
    for i in range(9):
        result.add(board[i][y])
        result.add(board[x][i])

    k, l = (x//3)*3, (y//3)*3
    for i in range(k,k+3):
        for j in range(l, l+3):
            result.add(board[i][j])
    result = list(set([1,2,3,4,5,6,7,8,9])-result)
    return result

board = [list(map(int,input().split())) for _ in range(9)]
result = []
flag = 0
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            result.append((i, j))
L = len(result)
used = [0]*(L)
solution(0)




