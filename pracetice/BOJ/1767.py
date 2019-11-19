import sys
import copy
sys.stdin = open('input.txt', 'r')


def back(x, k, N, cnt, used):
    global flag, Min

    if k == N:
        if Min > cnt:
            Min = cnt
        return
    else:
        for i in range(k, N):
            if used[i] ==0:
                used[i]= 1
                for j in range(4):
                    p, pcnt = solution(x, core[i], j, cnt)
                    if flag == 1:
                        flag = 0
                        continue
                    back(p, k+1, N, pcnt, used)
                used[i] = 0
                back(p, k + 1, N, pcnt, used)
    return

def solution(x, pos, direction):

    # 왼쪽으로 라인 연결
    if direction == 0:
        for i in range(pos[1]):
            if x[pos[0]][i]:
                for j in range(j,i):
                    x[pos[0]][i] = 0
                return -1
            else:
                x[pos[0]][i] = 2

    # 오른쪽 라인 연결
    elif direction == 1:
        for i in range(pos[1]+1,len(x)):
            if x[pos[0]][i]:

            else:
                cp[pos[0]][i] = 2
                pcnt += 1
                if pcnt > Min:
                    flag = 1

    # 위쪽라인 연결
    elif direction == 2:
        for i in range(pos[0]):
            if cp[i][pos[1]]:
                flag = 1
                return x, cnt
            else:
                cp[i][pos[1]] = 2
                pcnt += 1
                if pcnt > Min:
                    flag = 1
                    return x, cnt
    else:
        for i in range(pos[0]+1, len(x)):
            if cp[i][pos[1]]:
                flag = 1
                return x, cnt
            else:
                cp[i][pos[1]] = 2
                pcnt += 1
                if pcnt > Min:
                    flag = 1




T = int(input())
for test in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    flag = 0
    core = []
    Min = 150
    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j] == 1:
                core.append((i,j))
    used=[0]*N
    back(board, 0, len(core), 0, used)
    print(Min)