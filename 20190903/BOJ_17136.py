import pprint

def square(x,y,k):
    for i in range(x,x+k):
        for j in range(y,y+k):
            if not board[i][j]:
                return 0
    return 1

def square_l(x,y,k):
    for i in range(x,x+k):
        for j in range(y,y+k):
            if visit[i][j]:
                return 0
    return 1

def square_visit(x,y,k):
    for i in range(x,x+k):
        for j in range(y,y+k):
            visit[i][j] = 1

    return
def square_visit_return(x,y,k):
    for i in range(x,x+k):
        for j in range(y,y+k):
            visit[i][j] = 0
    return

def back(cnt,s,paper_cnt,p):
    global paper, Min

    if cnt >= Min or paper_cnt[0]>5 or paper_cnt[1]>5 or paper_cnt[2]>5 or paper_cnt[3]>5 or paper_cnt[4]>5:
        return
    if paper<=s+5:
        cnt += paper-s
        Min = min(Min, cnt)
        return
    else:
        for x in range(p,len(result)):
            i,j = result[x]
            if not visit[i][j]:
                for k in range(5, 1, -1):
                    if find[k-1][i][j]:
                        if square_l(i,j,k) and not used[x]:
                            used[x] = 1
                            square_visit(i,j,k)
                            paper_cnt[k-1] +=1
                            back(cnt+1,s+(k*k),paper_cnt,i+k)
                            square_visit_return(i,j,k)
                            paper_cnt[k - 1] -= 1
                            used[x] = 0
                            break
    return

board = [list(map(int,input().split())) for _ in range(10)]
visit = [[0]*10 for _ in range(10)]
paper = 0
result = []
Min = 0xffff
find=[[[0]*10 for _ in range(10)] for _ in range(5)]
paper_cnt = [0]*5
for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            paper += 1
            if i<6 and j < 6 and square(i,j,5):
                find[4][i][j] = 1
            if i<7 and j < 7 and square(i,j,4):
                find[3][i][j] = 1
            if i<8 and j < 8 and square(i,j,3):
                find[2][i][j] = 1
            if i<9 and j < 9 and square(i,j,2):
                find[1][i][j] = 1
            find[0][i][j] = 1
            result.append((i,j))
used = [0]*len(result)

back(0,0,paper_cnt,0)
if Min ==0xffff:
    print(-1)
else:
    print(Min)