import pprint
def solution(x, y, std_x, std_y, g):
    result = [(x, y), (std_x, std_y)]

    while g-1:
        g -= 1
        for i in range(len(result)-2, -1, -1):
            nx, ny = result[i]
            nx, ny = std_x + (ny-std_y), std_y - (nx-std_x)
            result.append(nx, ny)

    return result


board = [[[0]*101 for _ in range(101)] for _ in range(4)]
board[0][0][0] = 1
board[3][0][100] = 1
pprint.pprint(board)

N = int(input())

for _ in range(N):
    x, y, d, g = map(int, input().split())

