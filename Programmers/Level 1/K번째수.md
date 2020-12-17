K번째수
=================================================================

### 문제
https://programmers.co.kr/learn/courses/30/lessons/42748

### 코드

``` python
def solution(array, commands):
    answer = []

    num_list = array    # array 저장

    for i in range(len(commands)):
        # 슬라이스 지점과 원하는 위치 저장
        start = commands[i][0] - 1
        end = commands[i][1]
        index = commands[i][2] - 1

        # 잘라진 리스트를 정렬
        array = sorted(array[start:end])
        
        answer.append(array[index])
        array = num_list
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
```

### 풀이

1. commands에서 0번째는 시작지점, 1번째는 끝지점, 2번째는 원하는 값의 위치를 저장함
2. 잘라진 array 리스트를 정렬
3. index 위치의 값을 answer에 append
4. 위의 과정을 원하는만큼 반복

### 다른 사람 풀이

```python
def solution(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer
```
