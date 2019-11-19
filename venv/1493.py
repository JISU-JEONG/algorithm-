T = int(input())

for t in range(1, T+1):
    a, b = map(int,input().split())

    n, m = int(a**0.5), int(b**0.5)
    while  (n-1)*n//2>= a or a > n*(n+1)//2:
        n += 1

    while  (m-1)*m//2>= b or b > m*(m+1)//2:
        m += 1

    lotation = n+m+1

    result = lotation*(lotation+1)//2 - (lotation-((a+b)-(n*(n-1)+m*(m-1))//2))

    print('#{} {}'.format(t,result))
