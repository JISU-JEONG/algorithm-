from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
visit = [[0]*101 for _ in range(101)]
for _ in range(T):
    x, y, d, g = map(int, input().split())
    x, y = x,y
    dragon = deque()
    dragon.append((x, y))
    visit[y][x] = 1
    if d == 0:
        dragon.append((x+1, y))
        visit[y][x+1] = 1
    elif d == 1:
        dragon.append((x , y-1))
        visit[y-1][x] = 1
    elif d==2:
        dragon.append((x-1, y))
        visit[y][x-1] = 1
    else:
        dragon.append((x, y+1))
        visit[y+1][x] = 1
    k = 0
    while k < g:
        endx, endy = dragon[-1]
        for i in range(len(dragon)-2,-1,-1):
            x, y = dragon[i][0], dragon[i][1]
            nx, ny = endx+(endy-y), endy + (x-endx)
            dragon.append((nx, ny))
            visit[ny][nx] = 1
        k+=1

cnt = 0
for i in range(100):
    for j in range(100):
        if visit[i][j]:
            if visit[i][j]+visit[i+1][j] +visit[i][j+1]+ visit[i+1][j+1] == 4:
                cnt += 1

print(cnt)

'''
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)

3
3 3 0 1
4 2 1 3
4 2 2 1
'''