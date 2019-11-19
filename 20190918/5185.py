T = int(input())

for t in range(1, T+1):
    N, num = input().split()
    result = []

    for n in num:
        if '0'<=n<='9':
            result.append(ord(n)-ord('0'))
        else:
            result.append(ord(n) - ord('A')+10)
    print('#{} '.format(t),end='')
    for r in result:
        arr = [0]*4
        for i in range(3,-1,-1):
            arr[i]= r%2
            r//=2
        for i in range(4):
            print(arr[i],end='')
    print()
