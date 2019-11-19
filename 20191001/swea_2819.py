
def back(x,y,k, tmp):

    if k == 7:
        result.add(tmp)
    else:
        if x+1<4:
            back(x+1,y,k+1,tmp+numbers[x][y])
        if x-1>=0:
            back(x - 1, y, k+1,tmp + numbers[x][y])
        if y+1<4:
            back(x,y+1,k+1,tmp+numbers[x][y])
        if y-1>=0:
            back(x , y- 1, k+1,tmp + numbers[x][y])
T = int(input())

for t in range(1,T+1):
    result = set()
    numbers = [list(input().split()) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            back(i,j,0,'')
    print("#{} {}".format(t, len(result)))