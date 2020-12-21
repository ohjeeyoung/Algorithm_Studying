# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()
    boat = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        boat += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return boat

print(solution([70,50,80,50],100))
print(solution([70,80,50],100))
