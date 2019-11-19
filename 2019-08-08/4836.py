T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    map_list = [[0]*10 for _ in range(10)]
    N = int(input())
    for draw in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                map_list[i][j] += color
    purple = 0
    for row in map_list:
        if 3 in row:
            purple += row.count(3)

    print('#{} {}'.format(test_case, purple))