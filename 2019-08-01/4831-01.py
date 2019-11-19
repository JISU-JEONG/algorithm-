T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K, N, M = map(int, input().split())
    bus_stop = [0]*(N+1)
    bus_position = 0
    charge = list(map(int, input().split()))
    charge_num = 0
    for i in charge:
        bus_stop[i] = 1
    while bus_position + K < len(bus_stop)-1:
        if 1 not in bus_stop[bus_position+1:bus_position+K+1]:
            charge_num = 0
            break
        else:
            idx = 0
            bus_position += K
            for i in charge:
                if i <= bus_position:
                    idx = i
            bus_position = idx
            charge_num += 1

    print('#{} {}'.format(test_case, charge_num))