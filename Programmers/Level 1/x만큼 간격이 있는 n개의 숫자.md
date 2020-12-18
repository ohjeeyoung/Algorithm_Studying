x만큼 간격이 있는 n개의 숫자
=================================================================

### 문제
https://programmers.co.kr/learn/courses/30/lessons/12954

### 코드

``` python
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
```

### 풀이

x부터 x에 n을 곱한 수 까지를 리스트에 담는다.
