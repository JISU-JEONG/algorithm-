

def Zero(numbers):
    n = len(numbers)

    for i in range(1<<n):
        S = 0
        for j in range(n):
            if i & (1<<j):
                S += numbers[j]
        if S == 0 and i != 0:
            return True

    return False

numbers = list(map(int, input().split()))
print(Zero(numbers))
