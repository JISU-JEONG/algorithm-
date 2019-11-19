class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        pass

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None:   # 공백 리스트인지 항상 체크
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
            self.size += 1
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertfirst(self, node):
        if self.head is None:
            self.head = self.tail = node

    def deletelast(self):
        if self.head is None:
            return 'error'
        prev, cur = self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next

        if prev is None:
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev

        del cur

        self.size -= 1

    def deletefirst(self):
        if self.head is None:
            return
        cur = self.head
        if self.head == self.tail:
            self.head = self.tail = None

        else:

            self.head = cur.tail = None

        del cur
        self.size -= 1

    def insertAt(self, idx, node): # idx: 삽입 위치, node: 삽입 노드
        self.size += 1
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
                self.head = node
            elif cur is None:
                prev.next = self.tail = node
            else:
                node.next = cur
                prev.next = node


    def deleteAt(self, idx):
        if self.head is None:
            return
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1
            if prev is None:
                self.head = self.head.next
                return
            elif cur is None:
                return
            else:
                prev.next = cur.next
                self.size -= 1
            del cur

    def change(self, idx, data):
        if self.head is None:
            return
        else:
            cur = self.head
            while idx > 0 and cur is not None:
                cur = cur.next
                idx -= 1
            cur.data = data

    def printAt(self, idx):
        if self.size-1 < idx:
            return -1
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                cur = cur.next
                idx -= 1
            return cur.data



T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))
    dataList = List()
    for d in data:
        dataList.insertlast(Node(d))

    for m in range(M):
        string = list(input().split())
        if len(string)==2:
            commad, idx = string[0], string[1]
        else:
            commad, idx, value = string[0], string[1], string[2]
            value = int(value)
        idx = int(idx)
        if commad =='I':
            dataList.insertAt(idx, Node(value))
        elif commad == 'D':
            dataList.deleteAt(idx)
        else:
            dataList.change(idx, value)


    print('#{} {}'.format(t+1, dataList.printAt(L)))