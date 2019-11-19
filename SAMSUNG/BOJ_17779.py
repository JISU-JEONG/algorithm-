


def solve(choice):
    s = [0]*5
    x1, y1, x2, y2 = choice[0][0], choice[0][1], choice[1][0], choice[1][1]
    x3, y3, x4, y4 = choice[2][0], choice[2][1], choice[3][0], choice[3][1]
    # 첫번째 구역 더하기
    for i in range(x1):
        for j in range(y1+1):
            s[0] += board[i][j]
    k = 0
    for i in range(x1,x3):
        for j in range(y1-k):
            s[0] += board[i][j]
        k+=1
    # 두번째 구역 더하기
    for i in range(x1):
        for j in range(y1+1,N):
            s[1] += board[i][j]
    k = 0
    for i in range(x1,x2+1):
        for j in range(y1+k+1,N):
            s[1] += board[i][j]
        k+=1
    # 세번째 구역 더하기
    k = 0
    for i in range(x3, N):
        idx = y3+k
        if idx>=y4:
            idx=y4
        for j in range(idx):
            s[2] += board[i][j]
        k+=1
    # 네번째 구역 더하기
    k = 0
    for i in range(x4, N):
        idx = y2-k
        if idx <y4:
            idx = y4
        for j in range(idx,N):
            s[3] += board[i][j]
        k+=1
    for i in range(x4+1,N):
        for i in range(y4,N):
            s[3] += board[i][j]
    s[4] = total- sum(s)
    print(x1,y1,x2,y2,x3,y3,x4,y4)
    print(*s)
    return max(s)-min(s)



def back(x,y,choice):
    global Min
    if Min==0: return
    if len(choice) == 4:
        Min=min(Min,solve(choice))
    else:
        if len(choice)==0:
            for i in range(1, N-x):
                if y+i<N:
                    choice.append((x, y))
                    choice.append((x+i, y+i))
                    back(x,y,choice)
                    choice.pop()
                    choice.pop()
        else:
            x1,y1,x2,y2 = choice[0][0],choice[0][1],choice[1][0],choice[1][1]
            for i in range(1,N-x2):
                if y1-i>=0:
                    choice.append((x1+i, y1-i))
                    choice.append((x2+i, y2-i))
                    back(x, y, choice)
                    choice.pop()
                    choice.pop()



N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
total = 0
Min = 0xffffff
for i in range(N):
    for j in range(N):
        total+=board[i][j]

for i in range(N-2):
    for j in range(1,N-1):
        back(i,j,[])

print(Min)