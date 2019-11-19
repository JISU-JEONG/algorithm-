def back(choice):

    if len(choice) == M:
        print(*choice)
        return

    else:
        for i in range(1,N+1):
            choice.append(i)
            back(choice)
            choice.pop()


N, M = map(int, input().split())
back([])