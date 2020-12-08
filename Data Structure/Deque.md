## 데크(Deque)

> 데크는 양쪽 끝에서 삽입과 삭제를 허용하는 자료구조

> 스택과 큐를 동시에 구현할 때 사용

```python
# 데크

from collections import deque

dq = deque('data')  # 새 데크 객체를 생성
for elem in dq:
    print(elem.upper(), end='')
print()
dq.append('r')
dq.appendleft('k')
print(dq)
dq.pop()
dq.popleft()
print(dq[-1])
print('x' in dq)
dq.extend('structure')
dq.extendleft(reversed('python'))
print(dq)
```
- Time Complexity

리스트, 이중연결리스트로 구현한 경우: 스택과 큐의 각 연산의 수행시간과 동일

- 특징

사용 경우: 스크롤, 문서 편집기의 undo 연산, 웹 브라우저의 방문 기록 등
