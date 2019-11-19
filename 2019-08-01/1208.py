for test in range(10):
    tests = int(input())
    num_map = [int(x) for x in input().split()]

    while tests:
        max_index = num_map.index(max(num_map))
        min_index = num_map.index(min(num_map))
        if num_map[max_index] - num_map[min_index] <= 1:
            break
        num_map[max_index] -= 1
        num_map[min_index] += 1
        tests -=1

    max_index = num_map.index(max(num_map))
    min_index = num_map.index(min(num_map))
    print('#{} {}'.format(test+1, num_map[max_index] - num_map[min_index]))