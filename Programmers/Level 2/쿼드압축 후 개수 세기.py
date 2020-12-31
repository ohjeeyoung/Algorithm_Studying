# 쿼드압축 후 개수 세기
# https://programmers.co.kr/learn/courses/30/lessons/68936

def QuadTree(index, jndex, size, arr, answer):
    one = True
    zero = True
    
    for i in arr[index:index + size]:
        for j in i[jndex: jndex + size]:
            if j == 1:
                zero = False
            if j == 0:
                one = False
        
        if zero == False and one == False:
            break
    
    if one == True:
        answer[1] += 1
    
    elif zero == True:
        answer[0] += 1

    else:
        QuadTree(index, jndex, size // 2, arr, answer)
        QuadTree(index, jndex + size // 2, size // 2, arr, answer)
        QuadTree(index + size // 2, jndex, size // 2, arr, answer)
        QuadTree(index + size // 2, jndex + size // 2, size // 2,arr, answer)

def solution(arr):
    answer = [0,0]
    QuadTree(0, 0, len(arr), arr, answer)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
