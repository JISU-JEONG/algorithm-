T = int(input())

for t in range(1,T+1):
    N = float(input())
    k = 1
    flag = 0
    result = []
    while N:
        k = k/2
        if N>=k:
            result.append('1')
            N -= k
        else:
            result.append('0')
        if len(result) >12:
            flag=1
            break
    print('#{} overflow'.format(t)) if flag else print('#{}'.format(t),''.join(result))