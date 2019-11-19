import pprint
def R_solution(raw,col):
    MaxL = 0
    for i in range(col):
        cnt = dict()
        for j in range(raw):
            if board[i][j]:
                if cnt.get(board[i][j]):
                    cnt[board[i][j]] += 1
                else:
                    cnt[board[i][j]] = 1
        result = []
        for key, value in cnt.items():
           result.append((key,value))
        result.sort(key=lambda x : (x[1],x[0]))

        L = len(result)
        if L > 50: L=50
        MaxL = max(MaxL, 2*L)
        for k in range(L):
            board[i][2*k] =result[k][0]
            board[i][2 * k+1] = result[k][1]
        if 2*L < raw:
            for k in range(2*L,raw):
                board[i][k] = 0
    return MaxL,col

def C_solution(raw,col):
    MaxC = 0
    for i in range(raw):
        cnt = dict()
        for j in range(col):
            if board[j][i]:
                if cnt.get(board[j][i]):
                    cnt[board[j][i]] += 1
                else:
                    cnt[board[j][i]] = 1
        result = []
        for key, value in cnt.items():
           result.append((key,value))
        result.sort(key=lambda x : (x[1],x[0]))

        C = len(result)
        if C > 50: C = 50
        MaxC = max(MaxC, 2*C)
        for k in range(C):
            board[2*k][i] =result[k][0]
            board[2 * k+1][i] = result[k][1]
        if 2*C < col:
            for k in range(2*C,col):
                board[k][i] = 0
    return raw,MaxC



r, c, k  = map(int, input().split())
board = [[0]*100 for _ in range(100)]
inboard = [list(map(int,input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        board[i][j] =inboard[i][j]
time = 0
raw, col =3,3
while board[r-1][c-1] != k:
    if time >100: break
    time+=1
    # print('지금 col={} raw={}'.format(col,raw))
    if col >= raw:
        # print('R연산할꺼양')
        raw, col = R_solution(raw, col)
    else:
        # print('C연산할꺼양')
        raw, col = C_solution(raw, col)
    # print('===={}===='.format(time))
    # print(col, raw)
    # for i in range(50):
    #     for j in range(50):
    #         print(board[i][j],end=' ')
    #     print()

if time >100:
    time = -1
print(time)