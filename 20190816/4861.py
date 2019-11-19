T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    list_map = []
    find = 0
    compare_str = ''
    N, M= map(int, input().split())
    for i in range(N):
        list_map.append(input())
    #print(list_map)
    for i in list_map:
        if find == 1:
            break
        for j in range(N-M+1):
                compare_str = i[j:j+M]
                if compare_str == compare_str[::-1]:
                    find =1
                    break
    for i in range(N):
        if find == 1:
            break
        for j in range(N-M+1):
                compare_str = ''
                for k in range(M):
                    compare_str += list_map[j+k][i]
                if compare_str == compare_str[::-1]:
                    find =1
                    break
    print('#{} {}'.format(test_case, compare_str))