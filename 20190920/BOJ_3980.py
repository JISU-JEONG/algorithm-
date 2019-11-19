
def back(k, s):
    global Max
    if k == 11:
        Max = max(Max, s)
    else:
        for i in range(11):
            if not used[i] and player[k][i] != 0:
                used[i] = 1
                back(k+1,s+player[k][i])
                used[i] = 0

T = int(input())
for t in range(1, T+1):
    player = [list(map(int,input().split())) for _ in range(11)]
    used = [0]*11
    Max= 0
    back(0,0)
    print(Max)