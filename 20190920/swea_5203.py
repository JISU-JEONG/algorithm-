def find(card):
    for i in range(8):
        if card[i] and card[i+1] and card[i+2]:
            return 1
    return 0

T = int(input())

for t in range(1, T+1):
    card = list(map(int, input().split()))
    cnt = [[0]*10 for _ in range(2)]
    result = 0
    for i in range(12):
        cnt[i%2][card[i]] +=1
        if cnt[i%2][card[i]] ==3:
            result = i%2 +1
            break
        if find(cnt[i%2]):
            result = i % 2 + 1
            break
    print("#{} {}".format(t,result))