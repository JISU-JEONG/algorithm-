import time


def numbers(arr):

    cnt = 0
    for i in arr:
        if i != 0:
            cnt+=1
    cnt = cnt*2
    if cnt >100:
        cnt = 100
    return cnt

def R_func(board):

    cnt_list = [[0]*(max(map(max,board))+1) for _ in range(len(board))]

    # 카운트 세서 리스트를 만들어 준다.
    for i in range(len(board)):
        for num in board[i]:
            cnt_list[i][num] += 1
    result = [[0]*(max(map(numbers, cnt_list))) for _ in range(len(board))]
    for i in range(len(board)):
        k=0
        for j in range(1, max(cnt_list[i]) + 1):
            for idx, value in enumerate(cnt_list[i]):
                if j == value and idx and k < 100:
                    result[i][k] = idx
                    result[i][k+1] = value
                    k += 2

    return result




def C_func(board):
    cnt_list = [[0] * (max(map(max, board)) + 1) for _ in range(len(board[0]))]

    for i in range(len(board[0])):
        for j in range(len(board)):
            cnt_list[i][board[j][i]] += 1
    result = [[0] * len(board[0]) for _ in range(max(map(numbers, cnt_list)))]

    for i in range(len(board[0])):
        k=0
        for j in range(1, max(cnt_list[i]) + 1):
            for idx, value in enumerate(cnt_list[i]):
                if j == value and idx and k < 100:
                    result[k][i] = idx
                    result[k+1][i] = value
                    k += 2

    return result


r, c, k = map(int, input().split())
start = time.time()
cnt = 0
board = [list(map(int, input().split())) for _ in range(3)]

while True:
    if r-1<=len(board) and c-1 < len(board[0]) and board[r-1][c-1] == k:
        break
    cnt += 1
    if cnt > 100:
        cnt = -1
        break
    if len(board) >= len(board[0]):
        board = R_func(board)
    else:
        board = C_func(board)

print(cnt)
print('time :', time.time()-start)