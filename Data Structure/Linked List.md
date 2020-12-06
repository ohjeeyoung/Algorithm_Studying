## 연결리스트(Linked List)

1. 단순연결리스트(Singly Linked List)
> 단순연결리스트는 동적 메모리 할당을 이용해 노드들을 한 방향으로 연결하여 리스트를 구현하는 자료구조

```python
# 단순연결리스트

class SList:
    class Node:
        def __init__(self, item, link): # 노드 생성자(항목, 다음 노드 레퍼런스)
            self.item = item
            self.next = link
    
    def __init__(self): # 단순연결리스트 생성자(head, 항목 수(size))
        self.head = None
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_front(self, item):
        if self.is_empty(): # empty인 경우
            self.head = self.Node(item, None)   # head가 새 노드 참조
        else:
            self.head = self.Node(item, self.head)
        self.size += 1
    
    def insert_after(self, item, p):
        p.next = SList.Node(item, p.next)   # 새 노드가 p 다음 노드가 됨
        self.size += 1
    
    def delete_front(self):
        if self.is_empty(): # empty인 경우 에러 처리
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next  # head가 둘째 노드를 참조
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty(): # empty인 경우 에러 처리
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next # p 다음 노드를 건너뛰어 연결
        self.size -= 1

    def search(self, target):
        p = self.head   # head로부터 순차탐색
        for k in range(self.size):
            if target == p.item: return k   # 탐색 성공
            p = p.next
        return None # 탐색 실패
    
    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            p = p.next  # 노드들을 순차탐색

class EmptyError(Exception):    # underflow시 에러 처리
    pass


if __name__ == '__main__':
    s = SList() # 단순연결리스트 생성
    s.insert_front('orange')
    s.insert_front('apple')
    s.insert_after('cherry', s.head.next)
    s.insert_front('pear')
    s.print_list()
    print('cherry는 %d번째' % s.search('cherry'))
    print('kiwi는', s.search('kiwi'))
    print('배 다음 노드 삭제 후:\t\t', end='')
    s.delete_after(s.head)
    s.print_list()
    print('첫 노드 삭제 후:\t\t', end='')
    s.delete_front()
    s.print_list()
    print('첫 노드로 망고, 딸기 삽입 후:\t\t', end='')
    s.insert_front('mango')
    s.insert_front('strawberry')
    s.print_list()
    s.delete_after(s.head.next.next)
    print('오렌지 다음 노드 삭제 후:\t\t', end='')
    s.print_list()
```
- Time Complexity

search(): O(N)

삽입, 삭제: O(1)

단, insert_after(), delete_after()는 특정 노드 p의 레퍼런스(메모리 주소)가 주어지지 않으면 O(N)이 소요될 수 있음

- 특징

단순연결리스트에서는 삽입이나 삭제 시 항목들의 이동이 필요없다.

순차탐색(Sequential Search): 항목을 탐색하려면 항상 첫 노드부터 원하는 노드를 찾을 때까지 차례로 방문

사용: 스택과 큐, 해싱의 체이닝(Chaining), 트리, 비트코인의 블록체인 

2. 이중연결리스트(Doubly Linked List)
> 이중연결리스트는 각 노드가 두 개의 레퍼런스를 가지고 각각 이전 노드와 다음 노드를 가리키는 연결리스트
