
def solve(stack, choice):

    for n in choice:
        if pm[n] == '+':
            s = stack[n]+stack[n+1]
            stack[n] = s
            stack[n+1] = s
        elif pm[n] == '-':
            s = stack[n]-stack[n+1]
            stack[n] = s
            stack[n+1] = s
        elif pm[n] == '*':
            s = stack[n]*stack[n+1]
            stack[n] = s
            stack[n+1] = s
    return stack[choice[len(choice)-1]]



def back(choice,cnt):
    global Max
    if cnt == (N//2):
        stack = numbers.copy()
        num = solve(stack,choice)
        Max = max(Max, num)
    else:
        for i in range(N//2):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                back(choice,cnt+1)
                used[i] = 0
                choice.pop()


N = int(input())
string = input()
numbers = []
pm =[]
Max = -0xffffff
for c in string:
    if c.isdigit():
        numbers.append(int(c))
    else:
        pm.append(c)

used = [0]*(N//2)
back([],0)
print(Max)