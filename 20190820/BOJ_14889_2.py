import sys
import itertools

N = 0
arr = []


def team(member):
    allMember = [i for i in range(N)]
    start_team = []
    link_team = []

    ## 멤버 선택
    for i in allMember:
        if i in member:
            start_team.append(i)
        else:
            link_team.append(i)

    start_sum = 0
    for i in start_team:
        for j in start_team:
            start_sum += arr[i][j]

    link_sum = 0
    for i in link_team:
        for j in link_team:
            link_sum += arr[i][j]

    return abs(start_sum - link_sum)


def solve(members):
    ## 모든 경우의 수 뽑기
    combination_members = itertools.combinations(members, int(N / 2))
    print(list(combination_members))
    selected_members = list(combination_members)
    length = int(len(selected_members) / 2)

    minVal = sys.maxsize
    for member in selected_members[:length]:
        minus = team(member)

        if minVal > minus:
            minVal = minus

    print(minVal)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    members = [i for i in range(N)]

    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    solve(members)
