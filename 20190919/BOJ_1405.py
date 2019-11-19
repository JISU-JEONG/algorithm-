# def find(choice):
#     f

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def back(choice, k, x, y, p):
    global S
    if k == T:
        S+=p
    else:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (nx, ny) not in choice:
                choice.append((nx,ny))
                back(choice, k+1, nx, ny, p*(dir[i]/100))
                choice.pop()

T, E, W, S, N = map(int, input().split())
dir = [E, W, S, N]
S = 0
back([(0,0)], 0, 0, 0, 1)
print(S)