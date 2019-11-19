win = {1: 3, 2: 1, 3: 2}

def winner(i, j):
    if tonermenet[i] == tonermenet[j]:
        return i
    if win[tonermenet[i]] == tonermenet[j]:
        return i
    else:
        return j


def solution(start, end):
    if end - start < 2:
        return winner(start, end)
    else:
        return winner(solution(start, (start + end) // 2), solution((start + end) // 2 + 1, end))


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tonermenet = list(map(int, input().split()))
    tonermenet = [0] + tonermenet
    result = solution(1, N)

    print('#{} {}'.format(t, result))