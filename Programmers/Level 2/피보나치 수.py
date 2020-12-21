# 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    fibo = [0] * 100001
    fibo[1] = 1
    fibo[2] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n] % 1234567
