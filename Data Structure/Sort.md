## 정렬(Sort)


1. 선택정렬(Selection Sort)
> 선택정렬은 리스트에서 아직 정렬 안된 부분의 원소들 중에서 최솟값을 '선택'하여 정렬 안된 부분의
> 가장 왼쪽의 원소와 교환하는 정렬 알고리즘

```python
# 선택 정렬

def selection_sort(a):
    for i in range(0, len(a)-1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]

selection_sort(a)
print(a)
```
- Time Complexity

(N-1) + (N-2) + ... + 2 + 1 = N(N-1)/2 = O(N^2)

- 공간복잡도 

주어진 배열 안에서 교환(swap)을 통해 정렬이 수행되므로 O(n)

- 특징

항상 O(N^2) 수행시간이 소요

입력에 민감하지 않은(Input Insensitive) 알고리즘

불안정 정렬(Unstable Sort)

2. 삽입정렬(Insertion Sort)
> 삽입정렬은 리스트가 정렬된 부분과 정렬 안된 부분으로 나뉘며,
> 정렬 안된 부분의 가장 왼쪽 원소를 정렬된 부분에 '삽입'하는 방식의 정렬 알고리즘

```python
# 삽입정렬

def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]

insertion_sort(a)
print(a)
```

- Time Complexity

입력이 이미 정렬된 경우: N-1번

Worst Case: 1 + 2 + ... + (N-2) + (N-1) = N(N-1)/2 = O(N^2)

- 공간복잡도

주어진 배열 안에서 교환(swap)을 통해 정렬이 수행되므로 O(n)

- 특징

입력에 민감한(Input Sensitive) 알고리즘

안정 정렬(Stable Sort)

Worst Case: 선택정렬 > 삽입정렬

입력 크기가 작은 경우, 거의 정렬이 되어있는 경우에는 매우 좋은 성능을 보임

-> 재귀호출을 하지 않으며, 프로그램도 간단하기 때문


3. 힙정렬(Heap Sort)
> 힙정렬은 최대힙을 이용하여 루트를 힙의 가장 마지막 노드와 교환한 후 힙 크기를 1 감소시키고,
> 루트로부터 downheap 연산으로 힙 속성을 복원하는 과정을 반복하여 정렬하는 알고리즘

```python
# 힙정렬

def downheap(i, size):  # 루트로 올라온 키에 대해 힙속성을 회복시킴
    while 2*i <= size:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k += 1
        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k

def create_heap(a): # 정렬하기 전에 최대힙 만들기
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2+1)):
        downheap(i, hsize)

def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1] # 루트와 힙의 마지막 항목 교환
        downheap(1, N-1)
        N -= 1  # 힙 크기 1 감소

a = [-1, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', end='')
print(a)
create_heap(a)  # 힙 만들기
print('최대힙:\t', end='')
print(a)
heap_sort(a)
print('정렬 후:\t', end='')
print(a)


# 힙정렬 ver.2

import heapq

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]

heapq.heapify(a)    # 최소힙 만들기

s = []  # 정렬 결과를 저장 할 리스트
while a:
    s.append(heapq.heappop(a))  # 리스트 a의 가장 작은 항목을 삭제하여 리스트 s의 맨 뒤에 추가
print(s)
```

- Time Complexity

항상 O(NlogN)

- 특징

불안정 정렬(Unstable Sort)

루프 내의 코드가 길고, 비효율적인 캐시메모리 사용에 따라 대용량의 입력을 정렬하기에는 부적절

C/C++ 표준 라이브러리(STL)의 partial_sort(부분 정렬)는 힙정렬로 구현되어 있음

-> 부분 정렬: 가장 작은 k개의 원소만을 출력하는 정렬

4. 퀵정렬(Quick Sort)
> 퀵정렬은 입력의 맨 왼쪽 원소(피벗, Pivot)를 기준으로 피벗보다 작은 원소들과 큰 원소들을 각각 피벗의 좌우로 분할한 후,
> 피벗보다 작은 부분과 피벗보다 큰 부분을 각각 재귀적으로 정렬하는 알고리즘

```python
# 퀵정렬

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start   # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):   # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)


# 퀵정렬 ver.2

def quick_sort2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))
```

- Time Complexity

최선경우: O(NlogN)

평균경우: O(NlogN)

최악경우: O(N^2)

- 공간 복잡도

주어진 배열 안에서 교환(swap)을 통해 정렬이 수행되므로 O(N)

- 특징

Primitive Type 데이터를 정렬하는 자바 Standard Edition 6의 시스템 sort에 사용되고, C언어 라이브러리의 qsort에서 사용

Unix, g++, Visual C++ 등에서도 시스템 정렬로 사용

불필요한 데이터의 이동을 줄이고 먼 거리의 데이터를 교환할 뿐만 아니라, 한번 결정된 피벗들이 추후 연산에서 제외되는
특성 때문에, 시간 복잡도가 O(NlogN)을 가지는 다른 정렬 알고리즘과 비교했을 때도 가장 빠름

정렬하고자 하는 배열 안에서 교환하는 방식이므로, 다른 메모리 공간을 필요로 하지 않음

불안정 정렬(Unstable Sort)

정렬된 배열에 대해서는 불균형 분할에 의해 오히려 수행시간이 더 많이 걸림

5. 계수정렬(Countion Sort)
> 계수정렬은 키를 부분적으로 비교한느 정렬
> 키가 숫자로 되어있으면, 각 자릿수에 대해 키를 비교

```python
# 계수정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1    # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end='')    # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

```

- Time Complexity

데이터의 개수 N, 데이터(양수) 중 최댓값이 K 일 때 최악의 경우에도 수행시간 O(N+K)

- 공간 복잡도

K만큼의 배열을 만들어야 하므로 O(K)

- 특징

특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘

데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
