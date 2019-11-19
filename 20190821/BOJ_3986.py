T = int(input())
cnt = 0
for _ in range(T):
    test = input()
    A_cnt, B_cnt = 0, 0
    result = []
    for ch in test:
        if ch =='A':
            if not len(result):
                result.append(ch)
                A_cnt += 1
            else:
                if A_cnt:
                    A_cnt -= 1
                    if result.pop() != 'A':
                        break

        else:
            if not len(result):
                result.append(ch)
                B_cnt += 1
            else:
                if B_cnt:
                    B_cnt -= 1
                    if result.pop() != 'B':
                        break
    else:
        cnt += 1
print(cnt)