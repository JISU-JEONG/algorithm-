def solution(record):
    result = []
    answer = []
    user = dict()
    for string in record:
        command = list(string.split())
        if command[0] == 'Enter' or command[0] == 'Leave':
            result.append(command[0]+' '+command[1])
        if command[0] == 'Enter' or command[0] == 'Change':
            user[command[1]] = command[2]

    for r in result:
        command, userid = r.split()
        if command == 'Enter':
            answer.append('"{}님이 들어왔습니다."'.format(user[userid]))
        else:
            answer.append('"{}님이 나갔습니다."'.format(user[userid]))

    answer = '[' + ', '.join(answer)+']'
    return answer

a =solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])

print(a)