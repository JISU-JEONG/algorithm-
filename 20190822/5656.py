import pprint
import copy
def limit(x, y):
    if 0<=x<H and 0<=y<W:return 1
    else: return 0

def boom(x, y, board):

    global block_cnt
    r = board[x][y] - 1
    board[x][y] = 0
    block_cnt -= 1
    if r == 0:
        return
    else:
        for i in range(x-r, x+r+1):
            if x==i:
                continue
            if limit(i,y) and board[i][y] > 1:
                boom(i, y,board)
            elif limit(i,y) and board[i][y] == 1:
                board[i][y] = 0
                block_cnt -= 1
        for j in range(y - r, y + r + 1):
            if y==j:
                continue
            if limit(x,j) and board[x][j] > 1:
                boom(x, j,board)
            elif limit(x,j) and board[x][j] == 1:
                board[x][j] = 0
                block_cnt -= 1



def clear(board):
    for i in range(W):
        for j in range(H-1,0,-1):
            if board[j][i]==0:
                for k in range(j-1,-1,-1):
                    if board[k][i]:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
                        break



# def back(board, k, choice):
#     global cnt
#     if len(choice)==N:
#         block_cnt = cnt
#         for j in choice:
#             for i in range(H):
#                 if board[i][j]:
#                     block_cnt = boom(i, j, board, block_cnt)
#                     clear(board)
#                     break
#         print(block_cnt, choice)
#         pprint.pprint(board)
#
#     elif k < W:
#         if used[i] == 0:
#             used[i] = 1
#             choice.append(k)
#             back(board, k+1,choice)
#             used[i] =0

def back(choice):
    global block_cnt, cnt, Min
    if len(choice) == N:
        B = copy.deepcopy(board)
        block_cnt = cnt
        # print('start === ===== ====')
        # print(B)
        for i in choice:
            for j in range(H):
                if B[j][i]:
                    boom(j,i,B)
                    clear(B)
                    # print(B)
                    break

        if Min > block_cnt:
            Min = block_cnt
            # print(Min,'=========================',choice)
            # pprint.pprint(B)

    else:
        for i in range(W):
            choice.append(i)
            back(choice)
            choice.pop()

T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    Min = 1000000
    board = [list(map(int, input().split())) for _ in range(H)]
    cnt = 0
    used = [0] * W

    for i in range(H):
        for j in range(W):
            if board[i][j]:
                cnt += 1
    block_cnt = cnt
    back([])
    print('#{} {}'.format(t, Min))