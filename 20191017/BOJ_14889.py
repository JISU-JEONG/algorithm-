


def back(choice,k):
    global cnt
    if len(choice) ==N//2:
        print(*choice)
    else:
        for i in range(k,N):
            if not visit[i]:
                visit[i] = 1
                choice.append(i)
                back(choice,i+1)
                visit[i] = 0
                choice.pop()

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [0]*N
cnt=0
back([],0)
