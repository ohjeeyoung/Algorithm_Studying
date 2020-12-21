# 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    l = list(map(int, str(x)))
    Sum = sum(l)
    if x % Sum == 0:
        return True
    else:
        return False
