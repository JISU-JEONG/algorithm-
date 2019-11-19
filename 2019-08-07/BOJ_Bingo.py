import pprint

def check(board, key):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == key:
                board[i][j] = 0

    for i in range(5):
        C, R = 0, 0
        for j in range(5):
            C += board[i][j]
            R += board[j][i]
        if C == 0:
            cnt += 1
        if R == 0:
            cnt += 1
    L, R =0, 0
    for i in range(5):
        L += board[i][i]
        R += board[4-i][i]
    if L == 0:
        cnt += 1
    if R == 0:
        cnt += 1

    if cnt >= 3:
        return 1
    else:
        return 0

board = [list(map(int, input().split())) for _ in range(5)]
talk = [list(map(int, input().split())) for _ in range(5)]
flag = 0
tcnt = 0

for i in range(5):
    for j in range(5):
        tcnt += 1
        if check(board, talk[i][j]):
            flag = 1
            break
    if flag == 1:
        break


print(tcnt)