def back(choice):
    if len(choice) == 3:
        print(*choice)
    else:
        for i in range(1,6):
            choice.append(i)
            back(choice)
            choice.pop()

numbers = list(range(1, 6))
back([])