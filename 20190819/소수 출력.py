N = int(input())

numbers = [False, False] + [True]*(N-1)
primes=[]
for i in range(2, N+1):
  if numbers[i]:
    primes.append(i)
    for j in range(2*i, N+1, i):
        numbers[j] = False

print(primes)