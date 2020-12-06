## 큐(Queue)

> 큐는 삽입과 삭제가 양 끝에서 각각 수행되는 자료구조

> FIFO(First In First Out, 선입선출): 가장 먼저 들어온 것이 가장 먼저 나옴

```python
# 큐

# 큐-파이썬 리스트로 구현

def add(item):
    q.append(item)

def remove():
    if len(q) != 0:
        item = q.pop(0)
        return item

def print_q():
    print('front -> ', end='')
    for i in range(len(q)):
        print('{!s:<8}'.format(q[i]), end='')
    print(' <- rear')

q = []


# 큐-단순연결리스트로 구현

class Node:
    def __init__(self, item, n):
        self.item = item
        self.next = n

def add(item):
    global size
    global front
    global rear

    new_node = Node(item, None)
    if size == 0:
        front = new_node
    else:
        rear.next = new_node
    rear = new_node
    size += 1
    
def remove():
    global size
    global front
    global rear

    if size != 0:
        fitem = front.item
        front = front.next
        size -= 1
        if size == 0:
            rear = None
        return fitem

def print_q():
    p = front
    print('front: ', end='')
    while p:
        if p.next != None:
            print(p.item, '->   ', end='')
        else:
            print(p.item, end='')
        p = p.next
    print(' : rear')

front = None
rear = None
size = 0


add('apple')
add('orange')
add('cherry')
add('pear')
print('사과, 오렌지, 체리, 배 삽입 후: \t', end='')
print_q()
remove()
print('remove한 후:\t\t', end='')
print_q()
remove()
print('remove한 후:\t\t', end='')
print_q()
add('grape')
print('포도 삽입 후:\t\t', end='')
print_q()
```
- Time Complexity

add, remove 연산: O(1)

리스트 크기를 확대 또는 축소시키는 경우에 큐의 모든 항목들을 새 리스트로 복사해야 하므로 O(N)

- 특징

사용 경우: 버퍼, 마구 입력된 것을 처리하지 못하고 있는 상황, 이진트리의 레벨순회, BFS

CPU의 태스크 스케줄링(Task Scheduling), 네트워크 프린터, 실시간(Real-time) 시스템의 인터럽트(Interrupt) 처리, 다양한 이벤트 구동 방식(Event-driven) 컴퓨터 시뮬레이션, 콜 센터의 전화 서비스 처리 등
