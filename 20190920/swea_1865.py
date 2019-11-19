import sys
sys.stdin = open('1865.txt', 'r')

def back(k, p):
    global Max
    if Max >= p:
        return
    if k==N:
        Max = max(Max,p)
    else:
        for i in range(N):
            if not used[i] and board[k][i]>0:
                used[i] = 1
                back(k+1, p*board[k][i])
                used[i] = 0

T = int(input())


for t in range(1, T+1):
    N = int(input())
    Max = 0.0
    board = [list(map(lambda x: float(x)/100,input().split())) for _ in range(N)]
    used =[0]*N
    back(0,1)
    print('#{} '.format(t), end='')
    print('{0:.6f}'.format(Max*100))