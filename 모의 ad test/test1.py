
def back(cards, cnt):
    global Min
    if cnt > 5 or cnt>Min:
        return
    if cards == cards_s or cards == cards_r:
        Min =min(Min,cnt)
    else:
        for i in range(1, N):
            cards_c = suffle(cards,i)
            back(cards_c, cnt+1)



def suffle(cards, x):
    new_cards = [0]*N
    if x < N//2:
        j= 0
        for i in range(N):
            if i <N//2-x or i >= N//2+x:
                new_cards[i] = cards[i]
            else:
                if j % 2:
                    new_cards[i] = cards[N//2-x+j//2]
                    j += 1
                else:
                    new_cards[i] = cards[N // 2 + j // 2]
                    j += 1
    else:
        j = 0
        x = N-x-1
        for i in range(N):
            if i <N//2-x:
                new_cards[i] = cards[N//2+i]
            elif i >= N//2+x:
                new_cards[i] = cards[i-N//2]
            else:
                if j % 2:
                    new_cards[i] = cards[N//2+j//2+N//2-x]
                    j += 1
                else:
                    new_cards[i] = cards[j//2]
                    j += 1

    return new_cards


T = int(input())

for t in range(1, T+1):
    N = int(input())
    Min= 0xfffff
    cards = list(map(int, input().split()))
    cards_s = sorted(cards)
    cards_r = sorted(cards, reverse=True)
    back(cards, 0)
    if Min == 0xfffff:
        print('#{} {}'.format(t, -1))
    else:
        print('#{} {}'.format(t, Min))