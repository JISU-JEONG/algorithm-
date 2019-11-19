
def back(k, h):
    global Min
    if Min ==0:
        return
    if k ==N:
        if h>=H:
            Min = min(Min, h-H)
    else:
        back(k+1,h+board[k])
        back(k+1,h)

T = int(input())

for t in range(1, T+1):
    N, H = map(int,input().split())
    board = list(map(int, input().split()))
    Min = 0xffff
    back(0,0)
    print("#{} {}".format(t, Min))