from collections import deque

def bfs(start):
    # 첫 시작점을 방문 처리한다.
    visit[start] = 1
    # 첫 시작점을 통에 추가
    result.append(start)
    # deque을 사용해서 bfs를 하기위한 queue를 생성
    queue = deque()
    # 시작점을 추가해준다.
    queue.append(start)
    # 인접 노드를 방문점을 방문하는 bfs시작
    while queue:
        # queue의 맨 앞 원소를 빼온다. ( #popleft 사용)
        q = queue.popleft()
        # q의 연결된 노드를 방문
        for node in G[q]:
            # 방문한적이 없다면
            if not visit[node]:
                # 방문을 처리해준다.
                visit[node] = 1
                # queue에 방문한 원소를 추가해준다.
                queue.append(node)
                # result에 방문한 원소를 추가
                result.append(node)

# 1~7 까지 각각 노드의 연결점 표기
G = [
    [],
    [2, 3], # 1번 노드 2,3번 연결
    [1, 4, 5], # 2번 노드 1,4,5번 연결
    [1, 6, 7], # ...
    [2],
    [2],
    [3],
    [3],
]
# 각 노드의 갯수 만큼 방문점 생성
visit = [0]*8
# 각 방문순서를 담기 위한 통을 생성
result = []
# 1번에서 시작한다.
bfs(1)
# 결과를 표기
print(result)