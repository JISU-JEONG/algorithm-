
def solve(c1,c2):
    time1 = []
    time2 = []
    result = 0
    for i in c1:
        x = abs(stair[0][0]-person[i][0])+abs(stair[0][1]-person[i][1])
        time1.append(x)
    for i in c2:
        x = abs(stair[1][0]-person[i][0])+abs(stair[1][1]-person[i][1])
        time2.append(x)
    time1.sort()
    time2.sort()
    t1 = 0
    stack=[]
    stay=[]
    while time1 or stay:
        t1 += 1
        for i in range(len(stack)):
            stack[i] +=1
        while len(stack)>0 and stack[0]==board[stair[0][0]][stair[0][1]]:
                stack.pop(0)
        while stay and len(stack)<3:
            stack.append(0)
            stay.pop()
        while time1 and time1[0]<=t1:
            stay.append(0)
            time1.pop(0)

    if t1!=0:
        t1+=board[stair[0][0]][stair[0][1]]
    result = max(result,t1)
    t1= 0
    stack=[]
    stay=[]

    while time2 or stay:
        t1 += 1
        for i in range(len(stack)):
            stack[i] +=1
        while len(stack)>0 and stack[0]==board[stair[1][0]][stair[1][1]]:
                stack.pop(0)
        while stay and len(stack)<3:
            stack.append(0)
            stay.pop()
        while time2 and time2[0]<=t1:
            stay.append(0)
            time2.pop(0)


    if t1!=0:
        t1+=board[stair[1][0]][stair[1][1]]
    result = max(result, t1)

    return result

def back(k,c1,c2):
    global Min
    if k==L:
        Min=min(Min,solve(c1,c2))
    else:
        c1.append(k)
        back(k+1,c1,c2)
        c1.pop()
        c2.append(k)
        back(k + 1, c1, c2)
        c2.pop()


T = int(input())

for t in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    person = []
    stair = []
    Min = 0xffffff
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:continue
            if board[i][j]==1:
                person.append((i,j))
            else:
                stair.append((i,j))
    L = len(person)
    back(0,[],[])
    print("#{} {}".format(t,Min))