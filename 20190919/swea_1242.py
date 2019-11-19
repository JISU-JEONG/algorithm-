import sys; sys.stdin = open('1240.txt', 'r')

C = {
    (3, 2, 1, 1): 10,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}
def find_num(x):
    tmp = ''
    if '0' <= x <= '9':
        num = ord(x) - ord('0')
    else:
        num = ord(x) - ord('A') + 10
    for l in range(4):
        tmp += '1' if num & (1 << l) else '0'

    return tmp
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [input() for _ in range(N)]

    def find():
        S=0
        pwd = [0] * 8
        for i in range(N):
            j = M - 1
            while j >= 0:
                if board[i][j] != '0' and board[i-1][j] == '0':
                    tmp = find_num(board[i][j])
                    idx = 0
                    for k in range(7, -1, -1):
                        c2 = c3 = c4 = 0
                        while tmp[idx] == '0':
                            idx +=1
                            if idx ==4:
                                j-=1
                                idx, tmp = 0, find_num(board[i][j])
                        while tmp[idx] == '1':
                            c4, idx = c4 + 1, idx + 1
                            if idx ==4:
                                j-=1
                                idx, tmp = 0, find_num(board[i][j])
                        while tmp[idx] == '0':
                            c3, idx = c3 + 1, idx + 1
                            if idx == 4:
                                j -= 1
                                idx, tmp = 0, find_num(board[i][j])
                        while tmp[idx] == '1':
                            c2, idx = c2 + 1, idx + 1
                            if idx == 4:
                                j -= 1
                                idx, tmp = 0, find_num(board[i][j])
                        Min = min(c2, c3, c4)
                        c1 = 7*Min - (c2 + c3 + c4)
                        if Min!=0 and C.get((c1//Min, c2//Min, c3//Min, c4//Min)):
                            pwd[k] = C[(c1/Min, c2/Min, c3/Min, c4/Min)]%10
                    a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    b = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                    if (a * 3 + b) % 10 == 0:
                        S += (a + b)
                j -= 1
        return S

    print('#{} {}'.format(tc, find()))
