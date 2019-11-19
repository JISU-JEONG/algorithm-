
for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]

    ans = 0

    for idx in range(8):
        for s in range(8-N+1):
            e = s+N-1
            for i in range(N//2):
                if arr[idx][s+i] != arr[idx][e-i]: break
            else:
                ans += 1
            for i in range(N//2):
                if arr[s+i][idx] != arr[e-i][idx]: break
            else:
                ans += 1
    print(ans)