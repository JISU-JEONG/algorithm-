class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def printlist(self):
        if self.head is None:   # 공백 리스트인지 체크
            return

        cur = self.head
        print('[ ', end='')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')

    def insertlast(self, node):
        if self.head is None:   # 빈리스트
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertAt(self, idx, node):  # idx:삽입 위치, node:삽입 노드
        if self.head is None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None:
                node.next = cur
                node.data = cur.data + self.tail.data
                self.head = node
            elif cur is None:
                prev.next = self.tail = node
                node.data = prev.data + self.head.data
            else:
                node.data = cur.data + prev.data
                node.next = cur
                prev.next = node
            self.size += 1

    def dataAt(self, idx):
        if self.size < idx:
            return
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                cur = cur.next
                idx -= 1
            return cur.data


T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    result = List()
    data = list(map(int, input().split()))
    dataList = List()
    for i, d in enumerate(data):
        dataList.insertlast(Node(d))
    if N > dataList.size:
        N -= dataList.size
    for k in range(K):
        if N+M > dataList.size:
            N = N + M - dataList.size
        else:
            N += M
        dataList.insertAt(N,Node(0))
    print('#{}'.format(t+1),end=' ')
    if dataList.size < 10:
        for j in range(dataList.size):
            print(dataList.dataAt(dataList.size - 1 - j), end=' ')
    else:
        for j in range(10):
            print(dataList.dataAt(dataList.size-1-j), end=' ')
    print()