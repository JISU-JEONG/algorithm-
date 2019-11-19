from collections import deque

T = int(input())
for t in range(1, T+1):
    N, R = map(int, input().split())
    board = deque(map(int, input().split()))
    for i in range(R):
        board.append(board.popleft())
    print('#{} {}'.format(t, board[0]))