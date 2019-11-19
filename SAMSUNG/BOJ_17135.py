from collections import deque
import copy
dx = [0,-1,0]
dy = [-1,0,1]

def solution(choice, cnt,time,board):
    stack = []
    for c in choice:
        x,y = N, c
        visit= [[0]*M for _ in range(N)]
        queue = deque()
        queue.append((x,y))
        p, flag = 0, 0
        while queue and p < D and not flag:
            p += 1
            for _ in range(len(queue)):
                if flag: break
                x,y = queue.popleft()
                for i in range(3):
                    nx, ny = x+dx[i],y+dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if board[nx][ny] ==0 and not visit[nx][ny]:
                            queue.append((nx,ny))
                            visit[nx][ny] = 1
                        elif board[nx][ny] ==1 and not visit[nx][ny]:
                            flag = 1
                            if (nx,ny) not in stack:
                                stack.append((nx,ny))
                            break
    for x,y in stack:
        board[x][y] = 0
        cnt += 1
        time -=1
    return cnt,time

def move(board, time):
    time -= sum(board[N-1])
    board.pop()
    board.appendleft([0]*M)
    return time

def back(choice, k):
    global Max, attack
    if attack == Max:
        return
    if len(choice) == 3:
        time = attack
        cnt = 0
        new_board = copy.deepcopy(board)
        while time:
            cnt, time = solution(choice,cnt,time,new_board)
            time = move(new_board,time)
        Max = max(cnt, Max)
        return
    else:
        for i in range(k, M):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                back(choice,i+1)
                used[i] = 0
                choice.pop()

N, M, D = map(int, input().split())
board = deque(list(map(int, input().split())) for _ in range(N))
attack = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            attack +=1
Max = 0
used = [0]*M
back([],0)
print(Max)