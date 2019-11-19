def binary_seach(x, key):

    lo, hi = 0, len(x)-1

    while lo <= hi:
        mid = (lo+hi) >> 1

        if x[mid] == key:
            return 1
        elif x[mid] > key:
            hi = mid-1
        else:
            lo = mid+1
    return 0




N = int(input())

find = list(map(int, input().split()))

M = int(input())

cards = list(map(int, input().split()))
result = ['0']* len(cards)
find.sort()

for idx, card in enumerate(cards):
    if binary_seach(find, card):
        result[idx] = '1'

print(' '.join(result))