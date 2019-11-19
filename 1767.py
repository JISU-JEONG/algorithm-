import pprint

def check(i, board, x):
    global cnt
    # 왼쪽 편으로 라인 연결
    if i == 0:
        for j in range(core[x][1]):
            if board[core[x][0]][j] == 0:
                board[core[x][0]][j] = 2
                cnt+=1
            else:
                #만약 연결이 안될시 다시 복원해 준다.
                for k in range(j-1,-1,-1):
                    board[core[x][0]][k] = 0
                    cnt -= 1
                return 0

    # 오른 쪽 편으로 라인 연결
    elif i == 1:
        for j in range(N-1, core[x][1], -1):
            if board[core[x][0]][j] == 0:
                board[core[x][0]][j] = 2
                cnt += 1
            else:
                #만약 연결이 안될시 다시 복원해 준다.
                for k in range(j+1,N):
                    board[core[x][0]][k] = 0
                    cnt -= 1
                return 0

        # 아래 쪽 편으로 라인 연결
    elif i == 2:
        for j in range(N - 1, core[x][0], -1):
            if board[j][core[x][1]] == 0:
                board[j][core[x][1]] = 2
                cnt += 1
            else:
                # 만약 연결이 안될시 다시 복원해 준다.
                for k in range(j + 1, N):
                    board[k][core[x][1]] = 0
                    cnt -= 1
                return 0
        # 위 편으로 라인 연결
    else:
        for j in range(core[x][0]):
            if board[j][core[x][1]] == 0:
                board[j][core[x][1]] = 2
                cnt += 1
            else:
                # 만약 연결이 안될시 다시 복원해 준다.
                for k in range(j - 1, -1, -1):
                    board[k][core[x][1]] = 0
                    cnt -= 1
                return 0

    return 1

def check_return(i, board, x):
    global cnt
    # 왼쪽 편으로 라인 연결
    if i == 0:
        for j in range(core[x][1]):
            board[core[x][0]][j] = 0
            cnt -= 1

    # 오른 쪽 편으로 라인 연결
    elif i == 1:
        for j in range(N-1, core[x][1], -1):
            board[core[x][0]][j] = 0
            cnt -= 1

        # 아래 쪽 편으로 라인 연결
    elif i == 2:
        for j in range(N - 1, core[x][0], -1):
            board[j][core[x][1]] = 0
            cnt -= 1

        # 위 편으로 라인 연결
    else:
        for j in range(core[x][0]):
            board[j][core[x][1]] = 0
            cnt -= 1

    return 0



def back(k, used, board):
    global line, num,cnt
    if num == L and cnt > line:
        return
    if k == L:
        if num <= sum(used):
            if num == sum(used):
                if line > cnt:
                    line = cnt
            else:
                num = sum(used)
                line = cnt

    else:
        used[k] = 1
        for i in range(4):
            if check(i, board, k) == 1:
                back(k+1, used, board)
                check_return(i, board, k)
        used[k] = 0
        back(k+1, used, board)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    core = []
    line = 100000
    num, cnt = 0, 0
    for i in range(1, N):
        for j in range(1, N):
            if board[i][j] == 1:
                core.append((i,j))

    L = len(core)
    used = [0]*L

    back(0, used, board)

    print('#{} {}'.format(t,line))