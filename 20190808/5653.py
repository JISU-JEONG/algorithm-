import pprint

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(K):
    time = 0
    queue = start
    while time < K:
        time =+ 1

        # 지금 저장되어 있는 세포 위치들 (활성+비활성) 만큼 반복한다.
        for x, y in queue:
            #다음 세포 위치들을 저장 할것
            next_queue = []
            # 아직 n 이라면 비활성 상태
            if life[x][y]:
                next_queue.append((x,y))
            # 만약 0 활성 상태라면 4방향으로 퍼진다.(n 비활성 세포 ,0 활성 세포, -1 죽은 세포)
            elif life[x][y] == 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 방문한적이 없어야 된다.
                    if check[nx][ny] == 0:
                        #방문했다고 표기를 해준다.
                        check[nx][ny] = check[x][y]
                        next_queue.append((nx, ny))

        queue = next_queue.copy()

        for i in range(1000):
            for j in range(1000):
                if life[i][j] > 0:
                    life[i][j] -= 1





T = int(input())

for t in range(1, T+1):
    N, M, K =map(int, input().split())
    cnt = [0]*11
    check = [[0]*1000 for _ in range(1000)]
    life = [[-1] * 1000 for _ in range(1000)]
    start_x = 500-N>>1
    start_y = 500-M>>1
    start = []

    for i in range(start_x, start_x+N):
        cell = list(map(int, input().split()))
        for j in range(start_y, start_y+M):
            check[i][j] = cell[j-start_y]
            life[i][j] = cell[j-start_y]
            cnt[cell[j-start_y]] += 1
            start.append((i, j))

    solution(K)

    pprint.pprint(check)