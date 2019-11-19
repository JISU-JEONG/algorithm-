

def back(choice,k):
    global cnt
    if len(choice)==5:
        cnt+=1

    else:
        for i in range(4):
            for j in range(k,13):
                if not visit[j]:
                    visit[j]=1
                    choice.append(card[i][j])
                    back(choice,j+1)
                    choice.pop()
                    visit[j] = 0


visit = [0]*13
card = [list(range(13)) for _ in range(4)]
cnt = 0
back([],00)
print(cnt