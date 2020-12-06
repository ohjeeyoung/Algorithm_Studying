## 스택(Stack)

> 스택은 한 쪽 끝에서만 항목(item)을 삭제하거나 새로운 항목을 저장하는 자료구조

> LIFO(Last In First Out, 후입선출): 가장 나중에 들어온 것이 가장 먼저 나옴

```python
# 스택-파이썬 리스트로 구현

# 삽입 연산
def push(item):
    stack.append(item)

# top 항목 접근
def peek():
    if len(stack) != 0:
        return stack[-1]

# 삭제 연산
def pop():
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

stack = []
push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후:\t', end = '')
print(stack, '\t<-top')
print('top 항목: ', end = '')
print(peek())
push('pear')
print('배 push 후:\t\t', end = '')
print(stack, '\t<-top')
pop()
push('grape')
print('pop(), 포도 push 후:\t', end = '')
print(stack, '\t<-top')


# 스택-단순연결리스트로 구현

# 노드 클래스
class Node:
    def __init__(self, item, link): # Node 생성자
        self.item = item
        self.next = link

# push 연산
def push(item):
    global top
    global size
    top = Node(item, top)
    size += 1

# peek 연산
def peek():
    if size != 0:
        return top.item

# pop 연산
def pop():
    global top
    global size
    if size != 0:
        top_item = top.item
        top = top.next
        size -= 1
        return top_item

# 스택 출력
def print_stack():
    print('top ->\t', end='')
    p = top
    while p:
        if p.next != None:
            print(p.item, '-> ', end='')
        else:
            print(p.item, end='')
        p = p.next
    print()

top = None
size = 0

push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후:\t', end = '')
print_stack()
print('top 항목: ', end = '')
print(peek())
push('pear')
print('배 push 후:\t\t', end = '')
print_stack()
pop()
push('grape')
print('pop(), 포도 push 후:\t', end = '')
print_stack()
```
- Time Complexity

push, pop -> O(1)

동적 크기 조절은 스택(리스트)의 모든 항목들을 새 리스트로 복사 -> O(N)

- 특징

사용 경우: 함수의 콜스택, 문자열 역순 출력, 연산자 후위표기법, 괄호 짝 맞추기, 회문(Palindrome)
