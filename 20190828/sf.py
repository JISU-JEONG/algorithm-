from queue import PriorityQueue

arr = [(3, 5), (8, 9), (1, 4), (2, 6), (1,0)]

que = PriorityQueue()
for val in arr:
    que.put(val)

while not que.empty():
    print(que.get())