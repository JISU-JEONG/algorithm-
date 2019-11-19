T = int(input())

for t in range(1, T+1):
    N = list(input())
    l = len(N)
    flag =True

    for i in range(l>>1):
        if N[i] == '?' or N[l-i-1] == '?':
            N[i] = N[l-i-1] = '?'
        if N[i] != N[l-i-1]:
            flag = False
            break

    if flag:
        print('#{} Exist'.format(t))
    else:
        print('#{} Not exist'.format(t))
