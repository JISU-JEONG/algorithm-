from collections import deque

# 이 나무는 사계절을 보내며, 아래와 같은 과정을 반복한다.
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

def spring_summer():
    global tree_live
    # 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
    if tree_live == 0:
        return
    for i in range(N):
        for j in range(N):
            if len(tree[i][j]):
                # 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
                for k in range(len(tree[i][j])):
                    # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
                    if tree[i][j][k] <= ground[i][j]:
                        ground[i][j] -= tree[i][j][k]
                        tree[i][j][k] += 1
                    else:
                        # 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
                        # 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
                        # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
                        for _ in range(len(tree[i][j])-k):
                            ground[i][j] +=tree[i][j].pop()>>1
                            tree_live -= 1
                        break

def fall_winter():
    global tree_live
    if tree_live == 0:
        return
# 가을에는 나무가 번식한다.
# 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]
            if len(tree[i][j]):
                for k in range(len(tree[i][j])):
                    if tree[i][j][k] % 5 ==0:
                        # 어떤 칸 (r, c)와 인접한 칸은
                        # (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
                        # 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
                        # 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
                        # 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
                        for l in range(8):
                            x, y = i+dx[l], j + dy[l]
                            if 0<=x<N and 0<=y<N:
                                tree[x][y].appendleft(1)
                                tree_live += 1


# K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.
#
# 첫째 줄에 N, M, K가 주어진다.
N, M, K = map(int,input().split())
ground = [[5]*N for _ in range(N)]
tree = list(list(deque()*N for _ in range(N)) for _ in range(N))

tree_live = 0
# 둘째 줄부터 N개의 줄에 A배열의 값이 주어진다. r번째 줄의 c번째 값은 A[r][c]이다.
A = [list(map(int,input().split())) for _ in range(N)]
# 다음 M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다.
for _ in range(M):
    # 처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
    tree_live += 1

while K > 0:
    K -= 1
    spring_summer()
    fall_winter()

print(tree_live)