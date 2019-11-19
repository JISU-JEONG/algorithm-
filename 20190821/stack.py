
# C-style Stack code
# S = [0]*10
# top = -1
#
# def push(x):
#     global top
#     if top == 9:
#         return 0
#     top += 1
#     S[top] = x
#     return 1
#
# def pop(x):
#     global top
#     if top == -1:
#         return -1
#     else:
#         ret = S[top]
#         top -=1
#         return ret
#=================================================================================================
# Stack 사용 괄호 검사
# def find(string):
# #     for ch in string:
# #         if ch == '(':
# #             result.append(ch)
# #         else:
# #             if not len(result):
# #                 return -1
# #             else:
# #                 result.pop()
# #     if not len(result):
# #         return 1
# #     else:
# #         return -1
# #
# # string = input()
# # result = []
# #
# # ans = find(string)
# # print(ans)
#=================================================================================================
# 동적할당을 이용한 피보나치수열 함수
# def fibo(n):
#     for i in range(2,n+1):
#         dp.append(dp[i-1]+dp[i-2])
#     return dp[n]
#
#
# dp = [0,1]
# print(fibo(100))

#=================================================================================================
# 재귀적 함수 부분집합 구하기
# numbers = list(range(1,6))
# result = []
# def back(i, k):
#     if i == k:
#         print(*result)
#         return
#     else:
#         back(i+1,k)
#         result.append(numbers[i])
#         back(i+1,k)
#         result.pop()
#
# back(0,5)

#=================================================================================================
# memo = [-1]*1002
#
# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#     if memo[n] != -1:
#         return memo[n]
#     memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]
#
# print(fibo(1000))

# dfs(깊이우선탐색)
# def dfs(x):
#     # x가 들어오면 방문처리(1)을 해준다.
#     visited[x] = 1
#     # x를 결과 통에 담아준다.
#     result.append(x)
#     # x와 연결된 노드의 길이만큼 순차적으로 반복해준다.
#     for i in range(len(board[x])):
#         next_point = board[x][i]
#         # 만약 연결된 노드에 한번도 방문한적이 없으면 vidited[x] = 0 일때
#         if not visited[next_point]:
#             # 다음 점을 기준으로 들어간다.
#             dfs(next_point)
#
#
# board = [
#      [], # 인덱스 0번 => 연결된것 없음
#      [2, 3], # 인덱스 1번 => 2번, 3번 노드와 연결됨
#      [1, 4, 5], # 인덱스 2번 => 1번, 4번, 5번 노드와 연결됨
#      [1, 6, 7], # 인덱스 3번 => 1번, 6번 7번 노드와 연결됨
#      [2], # 인덱스 4번 => 2번 노드와 연결됨
#      [2], # 인덱스 5번 => 2번 노드와 연결됨
#      [3], # 인덱스 6번 => 3번 노드와 연결됨
#      [3] # 인덱스 7번 => 3번 노드와 연결됨
#     ]
# # 노드(점)의 갯수의 크기 만큼 방문처리 하기 위한 리스트 생성
# visited = [0]*8
# # 방문 순서를 기록하기 위한 결과 통
# result = []
# # 1번 부터 탐색을 시작
# dfs(1)
# # 기록된 방문순서를 출력한다.
# print(result)