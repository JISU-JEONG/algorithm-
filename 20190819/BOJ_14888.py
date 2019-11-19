def solution(choice):
    global M_num, N_num

    if len(choice) == N-1:
        S = numbers[0]
        for i in range(len(choice)):
            if choice[i] == 0:
                S += numbers[i+1]
            elif choice[i] == 1:
                S -= numbers[i+1]
            elif choice[i] == 2:
                S *= numbers[i + 1]
            else:
                if S > 0:
                    S //= numbers[i + 1]
                else:
                    S = (-S)//numbers[i+1]
                    S = -S
        if M_num < S:
            M_num = S
        if N_num > S:
            N_num =S
    else:
        for i in range(4):
            if selector[i] > 0:
                selector[i] -= 1
                choice.append(i)
                solution(choice)
                selector[i] += 1
                choice.pop()

N = int(input())
numbers = list(map(int, input().split()))

selector = list(map(int, input().split()))
M_num, N_num = -2000000000, 2000000000

solution([])
print(M_num)
print(N_num)