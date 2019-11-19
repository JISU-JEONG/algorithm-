T = int(input())

for t in range(T):
    string = ''
    n = int(input())
    for i in range(n):
        ch, num = input().split()
        string += ch*int(num)

    print('#{}'.format(t+1))
    while len(string):
        if len(string) >= 10:
            print(string[0:10])
            string = string[10:]
        else:
            print(sum_string)
            break