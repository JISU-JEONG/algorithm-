def rotation(ro , x):

    # 시계 방향으로 돌림
    if ro == 1:
        tmp = [x.pop()]
        x = tmp + x
    # 반시계 방향으로 돌림
    else:
        tmp = [x.pop(0)]
        x = x + tmp

    return x

def select(x, result):

    result.append(x)

    if x == 1:
        if t1[2] != t2[6]:
            result.append(2)
            if t2[2] != t3[6]:
                result.append(3)
                if t3[2] != t4[6]:
                    result.append(4)
    elif x == 2:
        if t1[2] != t2[6]:
            result.append(1)
        if t2[2] != t3[6]:
            result.append(3)
            if t3[2] != t4[6]:
                result.append(4)
    elif x == 3:
        if t3[2] != t4[6]:
            result.append(4)
        if t2[2] != t3[6]:
            result.append(2)
            if t1[2] != t2[6]:
                result.append(1)
    else:
        if t3[2] != t4[6]:
            result.append(3)
            if t2[2] != t3[6]:
                result.append(2)
                if t1[2] != t2[6]:
                    result.append(1)

    return result



T = int(input())

for t in range(1, T+1):
    K = int(input())

    t1 = list(map(int, input().split()))
    t2 = list(map(int, input().split()))
    t3 = list(map(int, input().split()))
    t4 = list(map(int, input().split()))

    S = 0

    for _ in range(K):
        pos, ro = map(int, input().split())
        selection = select(pos,[])
        for i in selection:
            if abs(pos-i)&1:
                d = -ro
            else:
                d = ro
            if i == 1:
                t1=rotation(d, t1)
            elif i == 2:
                t2=rotation(d, t2)
            elif i == 3:
                t3=rotation(d, t3)
            else:
                t4=rotation(d, t4)

    if t1[0] & 1:
        S += 1
    if t2[0] & 1:
        S += 2
    if t3[0] & 1:
        S += 4
    if t4[0] & 1:
        S += 8

    print('#{} {}'.format(t, S))



