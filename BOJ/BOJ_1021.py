def itoa(num):
    str_num = ''
    temp = []

    while num:
        temp.append(num%10)
        num //= 10

    while temp:
        str_num += chr(temp.pop()+ord('0'))

    return str_num

print(itoa(12345))