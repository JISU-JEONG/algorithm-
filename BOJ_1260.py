
def find(matrix, tmp, result):
    if not result:
        result.append(matrix.pop(0))
    for i in range(len(matrix)):
        if result[-1][1]==matrix[i][0]:
            result.append(matrix[i])
        else:
            tmp.append(matrix[i])
    if tmp:
        tmp.extend(result)
        return find(tmp,[],[])
    else:
        return result

T = int(input())

for t in range(1,1+T):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    matrix = []
    cnt = [0]*101
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                x, idx = 0,i
                while idx<N and board[idx][j]:
                    idx += 1
                    x+=1

                y, idy = 0, j
                while idy<N and board[i][idy]:
                    idy += 1
                    y+=1
                cnt[y] += 1
                matrix.append((x,y))
                for k in range(i,idx):
                    for l in range(j,idy):
                        board[k][l] = 0
    matrix = find(matrix,[],[])
    L = len(matrix)
    dp = [[0xffff]*L for _ in range(L)]
    for i in range(L):
        dp[i][i] = 0
    for i in range(L-2,-1,-1):
        for j in range(i+1,L):
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+matrix[i][0]*matrix[k][1]*matrix[j][1])

    print("#{} {}".format(t, dp[0][L-1]))


