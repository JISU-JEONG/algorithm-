def solution(N, stages):
    answer = [range(1, N + 1)]
    success = N
    fail = dict()
    cnt = [0] * (N + 2)

    for stage in stages:
        cnt[stage] += 1

    for i in range(1, N + 1):
        fail[i] = cnt[i] / success
        success -= cnt[i]

    vs = sorted(fail.values(), reverse=True)
    for v in vs:
        k = fail.
        answer.append(k)
        del fail[k]
    return answer