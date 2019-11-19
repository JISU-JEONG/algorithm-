# import collections
# dx = [0,0,1,1,1,-1,-1,-1]
# dy = [1,-1,1,-1,0,1,-1,0]
#
# z = ord('0')
#
# T = int(input())
#
# for t in range(1, T+1):
#     N, M = map(int,input().split())
#     castle = [list(input()) for _ in range(N)]
#     p = collections.deque()
#     for i in range(N):
#         for j in range(M):
#             if castle[i][j] =='.':
#                 castle[i][j] = 0
#                 p.append((i, j))
#             else:
#                 castle[i][j] = ord(castle[i][j]) -z
#     time = 0
#     while p:
#         time += 1
#         for _ in range(len(p)):
#             x,y = p.popleft()
#             if castle[x][y] <= 0:
#                 for i in range(8):
#                     nx, ny = x+dx[i],y+dy[i]
#                     if 0 <= nx < N and 0 <= ny < M:
#                         castle[nx][ny] -= 1
#                         if castle[nx][ny] ==0:
#                             p.append((nx,ny))
#
#     print("#{} {}".format(t, time-1))


import collections

dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,1,-1,0,1,-1,0]

z = ord('0')

N, M = map(int,input().split())
castle = [list(input()) for _ in range(N)]
p = collections.deque()
for i in range(N):
    for j in range(M):
        if castle[i][j] =='.':
            castle[i][j] = 0
            p.append((i, j))
        else:
            castle[i][j] = ord(castle[i][j]) -z
time = 0
while p:
    time += 1
    for _ in range(len(p)):
        x,y = p.popleft()
        if castle[x][y] <= 0:
            for i in range(8):
                nx, ny = x+dx[i],y+dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    castle[nx][ny] -= 1
                    if castle[nx][ny] ==0:
                        p.append((nx,ny))

print(time-1)

