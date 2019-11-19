from collections import deque
def solution(choice,cnt):
    time = 0
    k = 0
    field = [0]*3
    out = 0
    while time < N:
        if point[time][choice[k]] ==1:
            if field[2]==1: cnt+=1
            for i in range(1,-1,-1):
                field[i+1] = field[i]
            field[0] = 1
        elif point[time][choice[k]]==2:
            if field[2]==1:cnt+=1
            if field[1] == 1: cnt += 1
            field[2] = field[0]
            field[1] = 1
            field[0] = 0
        elif point[time][choice[k]]==3:
            if field[0]==1:
                cnt+=1
            if field[1]==1:
                cnt+=1
            if field[2]==1:
                cnt+=1
            field = [0,0,1]
        elif point[time][choice[k]]== 4:
            cnt += sum(field)
            cnt += 1
            field=[0]*3
        else:
            out +=1
            if out==3:
                time += 1
                out = 0
                field = [0]*3
        k+=1
        if k > 8:
            k=0
    return cnt

def back(choice):
    global Max
    if len(choice)==9:
        cnt = solution(choice,0)
        Max = max(Max,cnt)
    elif len(choice) == 3:
        choice.append(0)
        back(choice)
        choice.pop()
        return
    else:
        for i in range(1,9):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                back(choice)
                choice.pop()
                used[i] =0

N = int(input())
point =[list(map(int,input().split())) for _ in range(N)]
used=[0]*9
used[0]=1
Max=0
num=0
back([])
print(Max)
# solution([1 ,2 ,4 ,0 ,3 ,5, 6 ,7 ,8], 0)