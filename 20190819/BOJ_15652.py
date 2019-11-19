def back(choice,k):

    if len(choice) == M:
        print(*choice)
        return

    else:
        for i in range(k, N+1):
            choice.append(i)
            back(choice,i)
            choice.pop()


N, M = map(int, input().split())
back([],1)