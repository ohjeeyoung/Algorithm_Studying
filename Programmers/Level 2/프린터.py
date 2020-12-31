# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque([v, i] for i, v in enumerate(priorities))
    
    while len(que):
        item = que.popleft()

        if item[0] < max(que)[0]:
            que.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1,1,9,1,1,1],0))
