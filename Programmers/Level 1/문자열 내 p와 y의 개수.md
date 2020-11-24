문자열 내 p와 y의 개수
=================================================================

### 문제


### 코드

``` python
def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0

    s = list(s)

    for i in s:
        if i == 'p' or i == 'P':
            p_cnt += 1
        elif i == 'y' or i == 'Y':
            y_cnt += 1
    
    if p_cnt == y_cnt:
        answer = True
    else:
        answer = False

    return answer
```

### 풀이

1. 문자열로 입력되는 s를 list로 변환한다.
2. for문을 통해 s에 p 또는 y가 있는지 확인하고 p의 개수 p_cnt, y의 개수 y_cnt에 1씩 더해준다.
3. if문을 통해 p와 y의 개수가 같다면 answer에 True, 같지 않다면 False를 넣은 뒤 반환한다.
