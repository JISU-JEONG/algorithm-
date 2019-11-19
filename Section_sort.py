arr = [64, 25, 10, 22, 11]


def section_sort(numbers):
    # 첫번째 단계 [0,n-1]
    N = len(numbers)


    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if numbers[minIdx] > numbers[j]:
                minIdx = j
        numbers[i], numbers[minIdx] = numbers[minIdx], numbers[i]

    return numbers

print(section_sort(arr))