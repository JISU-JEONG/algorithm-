def back(choice, k):

    if len(choice) == 3:
        print(choice)
        return
    else:
        for i in range(k,7):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                back(choice, i+1)
                used[i] = 0
                choice.pop()

numbers = list(range(1,7))
used = [0]*7
back([],1)