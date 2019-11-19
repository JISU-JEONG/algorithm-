
def back(choice):
    global Max
    if len(choice) == N:
        S = 0
        for i in range(N-1):
            S += abs(board[choice[i]]-board[choice[i+1]])
        Max = max(S, Max)

    else:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                back(choice)
                choice.pop()
                used[i] = 0

N = int(input())
board = list(map(int, input().split()))
used = [0]*N
Max = -0xffff
back([])
print(Max)