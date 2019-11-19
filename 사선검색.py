




N, M = len(arr), len(arr[0])
for diag in range(N + M -1):

    x = 0 if diag < M else (diag - M + 1) # x의 시작 좌표
    y = diag if diag < M else M -1 # y의 시작 좌표

    while x < N 