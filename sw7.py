def my_sort(nasa, result, temp):
    if not result:
        result.append(nasa[0])
        result.append(nasa[1])
    for i in range(2, len(nasa), 2):
        if nasa[i] == result[-1]:
            result.append(nasa[i])
            result.append(nasa[i + 1])
        else:
            temp.append(nasa[i])
            temp.append(nasa[i + 1])
    if temp:
        temp.extend(result)
        result.clear()
        return my_sort(temp, result, [])
    else:
        return result


T = int(input())
for t in range(T):
    result = []
    temp = []
    N = int(input())
    nasa = list(map(int, input().split()))
    print('#{}'.format(t + 1), end=' ')
    for num in my_sort(nasa, result, temp):
        print(num, end=' ')
    print()