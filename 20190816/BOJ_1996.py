T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = []
    M += 1
    while arr:
        m_num = max(arr)
        if arr[0] == m_num:
            queue.append(arr.pop(0))
            if M == len(arr):
                break
        else:
            arr.append(arr.pop(0))
            M -= 1
            if M < len(queue)+1:
                M = N

    print(M)