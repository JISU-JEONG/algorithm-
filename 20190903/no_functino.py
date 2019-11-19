import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [0,1,1]
dy = [1,0,1]

def back(x, y, d):
    global cnt
    if x==N-1 and y==N-1:
        cnt += 1
    else:
        for i in direction[d]:
            if i == 0:
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if not board[nx][ny]:
                        back(x, y+1, i)
            elif i == 1:
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if not board[nx][ny]:
                        back(x+1, y, i)
            else:
                flag = 0
                for j in range(3):
                    nx, ny = x + dx[j], y + dy[j]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny]:
                            flag =1
                    else:
                        flag =1
                        break
                if flag == 0:
                    back(x + 1, y+1, i)




# 0: 가로 1: 세로 2: 대각선
N = int(input())
cnt = 0
direction = { 0: [0,2], 1: [1,2], 2: [0,1,2]}
board = [list(map(int, input().split())) for _ in range(N)]
board[0][0], board[0][1] = 1, 1
back(0, 1, 0)

print(cnt)
