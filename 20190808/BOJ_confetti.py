board = [[0]*101 for _ in range(101)]

N = int(input())
result =[0]*N

for i in range(N):
    pos = list(map(int,input().split()))
    for x in range(pos[0],pos[0]+ pos[2]):
        for y in range(pos[1],pos[1]+ pos[3]):
            if not board[x][y]:
                board[x][y] = i+1
                result[i] +=1
            else:
                result[board[x][y]-1] -= 1
                board[x][y] = i+1
                result[i] += 1
print(*result[:],sep='\n')
