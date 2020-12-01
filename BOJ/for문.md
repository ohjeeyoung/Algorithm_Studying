## for문 문제풀이
--------------------------------------------------------
- [2438번](#2438번)
- [2439번](#2439번)
- [2739번](#2739번)
- [2741번](#2741번)
- [2742번](#2742번)
- [8393번](#8393번)
- [10871번](#10871번)
- [10950번](#10950번)
- [11021번](#11021번)
- [11022번](#11022번)
- [15552번](#15552번)






### 2438번
별 찍기-1

#### 문제
https://www.acmicpc.net/problem/2438

#### 코드

``` python
N = int(input())

for i in range(N):
    print("*"*(i+1))
```
=====================================================

### 2439번
별 찍기-2

#### 문제
https://www.acmicpc.net/problem/2439

#### 코드

``` python
N = int(input())

for i in range(1,N+1):
    print(" " * (N-i) + "*" * (i))
```
=====================================================

### 2739번
구구단

#### 문제
https://www.acmicpc.net/problem/2739

#### 코드

``` python
N = int(input())

for i in range(1,10):
    print(N, '*', i, '=', N*i)
```
=====================================================

### 2741번
N 찍기

#### 문제
https://www.acmicpc.net/problem/2741

#### 코드

``` python
N = int(input())

for i in range(N):
    print(i+1)
```
=====================================================


### 2742번
기찍 N

#### 문제
https://www.acmicpc.net/problem/2742

#### 코드

``` python
N = int(input())

for i in range(N):
    print(N-i)
```
=====================================================

### 8393
합

#### 문제
https://www.acmicpc.net/problem/8393

#### 코드

``` python
n = int(input())

answer = 0

for i in range(1, n+1):
    answer += i

print(answer)
```
=====================================================

### 10871번
X보다 작은 수

#### 문제
https://www.acmicpc.net/problem/10871

#### 코드

``` python
N, X = map(int, input().split())

number_list = list(map(int, input().split()))
answer = []

for i in number_list:
    if i < X:
        answer.append(str(i))
        # print(i, end = ' ')

print(' '.join(answer))
```
=====================================================

### 10950번
A+B-3

#### 문제
https://www.acmicpc.net/problem/10950

#### 코드

``` python
T = int(input())

answer = []

for _ in range(T):
    A, B = input().split(' ')
    answer.append(int(A)+int(B))

for result in answer:
    print(result)
```
=====================================================

### 11021번
A+B-7

#### 문제
https://www.acmicpc.net/problem/11021

#### 코드

``` python
T = int(input())

answer = []

for _ in range(T):
    A, B = input().split(' ')
    answer.append(int(A)+int(B))

for i in range(T):
    print("Case #%d:" % (i+1), answer[i])
```
=====================================================

### 11022번
A+B-8

#### 문제
https://www.acmicpc.net/problem/11022

#### 코드

``` python
T = int(input())

A_num = []  # A값 저장 리스트
B_num = []  # B값 저장 리스트
answer = []

for _ in range(T):
    A, B = input().split(' ')
    A_num.append(int(A))
    B_num.append(int(B))
    answer.append(int(A)+int(B))

for i in range(T):
    print("Case #%d:"%(i+1), A_num[i], "+", B_num[i], "=", answer[i])
```
=====================================================

### 15552번
빠른 A+B

#### 문제
https://www.acmicpc.net/problem/15552

#### 코드

``` python
import sys

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    A, B = sys.stdin.readline().split(' ')
    answer.append(int(A)+int(B))

for result in answer:
    print(result)
```
