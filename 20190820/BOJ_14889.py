import sys

input = sys.stdin.readline

def back(team1, team2, k):
    global Mimnum
    if len(team1)==len(team2) == N//2:
        S = 0
        for i in range(N//2):
            for j in range(N//2):
                S += (team[team1[i]][team1[j]]-team[team2[i]][team2[j]])

        if abs(S) < Mimnum:
            Mimnum = abs(S)

    else:
        if len(team1) >N//2 or len(team1) >N//2:
            return
        for i in range(k, N):
            team1.append(i)
            back(team1, team2, i+1)
            team1.pop()
            team2.append(i)
            back(team1, team2, i+1)
            team2.pop()

N = int(input())

team = [list(map(int, input().split())) for _ in range(N)]
Mimnum = 100000

back([0], [], 1)

print(Mimnum)

