# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
        except IndexError:
            return -1
        cnt += 1
    return cnt

print(solution([1,2,3,9,10,12], 7))
