arr = 'ABC'; N = len(arr)
bits = [0] * N

def subset(k, n):
    if k == n:
        print(bits)
        return

    bits[k] = 1; subset(k +1, n) # 왼쪽
    bits[k] = 0; subset(k + 1, n) # 오른쪽

subset(0, N)