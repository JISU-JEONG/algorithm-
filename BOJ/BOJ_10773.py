
while True:
    is_balance = 0
    string = input()
    str_box = []
    if string =='.':
        break
    for ch in string:
        if ch == '[' or ch == '(':
            str_box.append(ch)
        elif ch == ']':
            if len(str_box) == 0 or str_box.pop() != '[':
                is_balance = 1
                break
        elif ch == ')':
            if len(str_box) == 0 or str_box.pop() != '(':
                is_balance = 1
                break
    if len(str_box):
        is_balance = 1

    if is_balance:
        print('no')
    else:
        print('yes')

