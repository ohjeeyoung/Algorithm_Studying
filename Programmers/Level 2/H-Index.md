H-Index
=================================================================

### 문제
https://programmers.co.kr/learn/courses/30/lessons/42747

### 코드

``` python
def solution(citations):
    answer = 0

    citations.sort()
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            answer += l-i
            return answer

    return answer


print(solution([3, 0, 6, 1, 5]))
print(solution([3, 0, 6, 1, 5, 6]))
print(solution([1, 2, 3, 4, 5, 6]))
```
### 풀이

1. citations를 정렬
2. citations의 값이 l-i 보다 크거나 같다면 l-i 수 만큼의 인용된 논문이 그만큼 있다는 것
