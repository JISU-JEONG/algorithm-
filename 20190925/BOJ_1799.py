
def check(idx,result,n):
    for i in range(L):
        if i==idx:
            continue
        else:
            if abs(p[n][idx][0]-p[n][i][0]) == abs(p[n][idx][1]-p[n][i][1]) and not used[i]:
                result.append(i)

def back(k, cnt,n):
    global Max
    if k == L:
        Max = max(Max, cnt)
    else:
        if not used[k]:
            result = []
            used[k] = 1
            check(k,result,n)
            for r in result:
                used[r] =1
            back(k+1, cnt+1,n)
            used[k] = 0
            for r in result:
                used[r] =0
        back(k+1, cnt,n)

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
p = [[],[]]
result = 0
Max = 0
for i in range(N):
    for j in range(N):
        if board[i][j] and (i+j)&1:
            p[(i+j)&1].append((i,j))
        elif board[i][j]:
            p[(i+j)&1].append((i,j))
for i in range(2):
    Max = 0
    L = len(p[i])
    used =[0]*L
    back(0,0,i)
    result += Max
print(result)