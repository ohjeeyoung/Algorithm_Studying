# 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    cnt = 0
    while num != 1:
        if cnt == 500 and num != 1:
            return -1
        if num % 2 == 0:
            num /= 2
            cnt += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            cnt += 1
    return cnt
