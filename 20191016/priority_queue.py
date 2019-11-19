import queue


q = queue.PriorityQueue()
q.put((1,'apple'))
q.put((1,'Apple'))
q.put((1,'banana'))
q.put((1,'Banana'))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
