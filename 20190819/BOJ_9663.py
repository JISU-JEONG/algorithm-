import datetime
def N_Queen(col, choice):

    global cnt
    if len(choice) == N:
        cnt += 1

    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                choice.append(i)
                if len(choice)==1:
                    N_Queen(col+1, choice)
                elif len(choice) > 1:
                    flag = 0
                    for j in range(len(choice)-1):
                        if abs(choice[-1] - choice[j]) == len(choice)-1-j:
                            flag =1
                            break
                    if flag == 0:
                        N_Queen(col+1, choice)
                used[i] = 0
                choice.pop()

N = int(input())
a = [13,73712]
board = [[0]*N for _ in range(N)]
used = [0]*N
cnt = 0

start = datetime.datetime.now()
N_Queen(0, [])
end = datetime.datetime.now()
print(cnt)
print(end-start)
