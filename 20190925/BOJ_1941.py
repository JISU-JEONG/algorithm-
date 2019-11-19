dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(point):
    visit = [[0]*5 for _ in range(5)]
    cnt = 1
    sx,sy = point[0]
    visit[sx][sy] = 1
    queue = [(sx,sy)]
    while queue:
        if cnt ==7:
            break
        x, y =queue.pop(0)
        for i in range(4):
            nx,ny = x+dx[i],y +dy[i]
            if 0<=nx<5 and 0<=ny<5:
                if not visit[nx][ny] and (nx,ny) in point:
                    visit[nx][ny] = 1
                    queue.append((nx,ny))
                    cnt += 1
    if cnt == 7:
        return 1
    else:
        return 0


def back(k, choice):
    global result
    if len(choice) == 7:
        point =[]
        y_cnt = 0
        for num in choice:
            x,y = num//5,num%5
            point.append((x,y))
            if board[x][y] == 'Y':
                y_cnt +=1
        if y_cnt>=4:
            return
        else:
            if bfs(point):
                result += 1
    else:
        for i in range(k,25):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                back(i+1,choice)
                choice.pop()
                used[i] = 0


board = [''.join(input().split()) for _ in range(5)]
used = [0]*25
result = 0
back(0,[])
print(result)