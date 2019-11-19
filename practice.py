import sys
input = sys.stdin.readline

def dfs(s):
    visit[s] = 1
    
        for i in board[s]:
            if not visit[i]:
                stack.append(i)
                visit[i] = 1
        else:
            s = stack.pop()

N, M = map(int, input().split())
board = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)

visit = [0]*(N+1)
cnt = 0
for i in range(1, N+1):
    if not visit[i]:
        cnt+=1
        dfs(i)

print(cnt)