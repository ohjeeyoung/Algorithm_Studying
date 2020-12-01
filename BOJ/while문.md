## while문 문제풀이
--------------------------------------------------------
- [1110번](#1110번)
- [10951번](#10951번)
- [10952번](#10952번)

----------------------------------------------------




### 1110번
#### 더하기 사이클

#### 문제
https://www.acmicpc.net/problem/1110

#### 코드

``` python
N = int(input())
cnt = 0
new_num = N

while True:
    new_num = (new_num%10)*10 + (new_num//10 + new_num%10)%10

    cnt += 1

    if N == new_num:
        break

print(cnt)
```
----------------------------------------------------

### 10951번
#### A+B-4

#### 문제
https://www.acmicpc.net/problem/10951

#### 코드

``` python
while(True):
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
```
----------------------------------------------------

### 109529번
#### A+B-5

#### 문제
https://www.acmicpc.net/problem/10952

#### 코드

``` python
while(True):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
```
