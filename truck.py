from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    result = deque()
    time = []
    while truck_weights or time:
        while weight > sum(result) and len(truck_weights):
            result.append(truck_weights.popleft())
            time.append(0)
        if weight < sum(result):
            truck_weights.appendleft(result.pop())
            time.pop()
        for i in range(len(time)):
            time[i] += 1
        while len(time) != 0 and time[0] == bridge_length:
            time.pop(0)
            result.popleft()
        answer += 1
    return answer+1


a = solution(100, 100, [10])
print(a)