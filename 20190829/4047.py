T = int(input())

for t in range(1, T+1):
    string = input()
    mode = {'S': 0,'D':1,'H':2,'C':3}
    error = 0
    visit = [[0]*14 for _ in range(4)]
    for i in range(len(string)//3):
        f = string[3*i]
        number = int(string[3*i+1:3*i+3])
        visit[mode[f]][number] += 1
        if visit[mode[f]][number] > 1:
            error = 1
            break
    if error:
        result = 'ERROR'
        print('#{} ERROR'.format(t))
    else:
        result = list(map(lambda x : 13-sum(x),visit))
        print('#{} {} {} {} {}'.format(t , *result))
