import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int ,input().split())
    flag = 0
    board = [list(map(int, input())) for _ in range(N)]
    dic_c = {
        '0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9
    }
    for i in range(N):
        if flag: break
        for j in range(M):
            if board[i][j]:
                start = [i,j]
                for k in range(j+1,M):
                    if board[i][k]:
                        end = [i,k]
                flag =1
                break
    p = 56-end[1]+start[1]-1
    code = ['0']*p
    for j in range(start[1],end[1]+1):
        code.append(str(board[start[0]][j]))
    result =[]
    for i in range(8):
        result.append(dic_c[''.join(code[7*i:7*i+7])])
    S = 0
    for i in range(8):
        if i&1:
            S+=result[i]
        else:
            S +=3*result[i]
    print('#{} 0'.format(t)) if S%10 else print('#{} {}'.format(t,sum(result)))