import sys
sys.setrecursionlimit(10**9)

def omok1(x, y, k, cnt):
    if 0 <= x < 19 and 0 <= y < 19:
        visit_c[x][y] = 1
    if x<0 or 19<= x or y<0 or y >=19 or board[x][y] != k:
        if 0 <= x < 19 and 0 <= y < 19:
            visit_c[x][y] = 0
        if cnt == 5: return 1
        else: return 0
    else: return omok1(x+1, y, k,cnt+1)

def omok2(x, y, k, cnt):
    if 0<= x <19 and 0<= y <19:
        visit_r[x][y] = 1
    if x<0 or 19<= x or y<0 or y >=19 or board[x][y] != k:
        if 0 <= x < 19 and 0 <= y < 19:
            visit_r[x][y] = 0
        if cnt == 5: return 1
        else: return 0
    else: return omok2(x, y+1, k,cnt+1)

def omok3(x, y, k, cnt):
    if 0 <= x < 19 and 0 <= y < 19:
        visit_d1[x][y] = 1
    if x<0 or 19<= x or y<0 or y >=19 or board[x][y] != k:
        if 0 <= x < 19 and 0 <= y < 19:
            visit_d1[x][y] = 0
        if cnt == 5: return 1
        else: return 0
    else:
        return omok3(x+1, y+1, k,cnt+1)

def omok4(x, y, k, cnt):
    if 0 <= x < 19 and 0 <= y < 19:
        visit_d2[x][y] = 1
    if x<0 or 19<= x or y<0 or y >=19 or board[x][y] != k:
        if 0 <= x < 19 and 0 <= y < 19:
            visit_d2[x][y] = 0
        if cnt == 5: return 1
        else: return 0
    else: return omok4(x+1, y-1, k,cnt+1)

board = [list(map(int, input().split())) for _ in range(19)]
visit_r = [[0]*19 for _ in range(19)]
visit_c = [[0]*19 for _ in range(19)]
visit_d1 = [[0]*19 for _ in range(19)]
visit_d2 = [[0]*19 for _ in range(19)]
flag = 0

for i in range(19):
    if flag == 1: break
    for j in range(19):
        if flag == 1: break
        if board[i][j]:
            if not visit_c[i][j]:
                result = omok1(i, j, board[i][j], 0)
                if result == 1:
                    flag =1
                    pos = (i+1,j+1)
                    type = board[i][j]
                    break
            if not visit_r[i][j]:
                result = omok2(i, j, board[i][j], 0)
                if result == 1:
                    flag =1
                    pos = (i+1,j+1)
                    type = board[i][j]
                    break
            if not visit_d1[i][j]:
                result = omok3(i, j, board[i][j], 0)
                if result == 1:
                    flag =1
                    pos = (i+1,j+1)
                    type = board[i][j]
                    break
            if not visit_d2[i][j]:
                result = omok4(i, j, board[i][j], 0)
                if result == 1:
                    flag =1
                    pos = (i+5,j-3)
                    type = board[i][j]
                    break
if flag:
    print(type)
    print(*pos)
else:
    print(0)