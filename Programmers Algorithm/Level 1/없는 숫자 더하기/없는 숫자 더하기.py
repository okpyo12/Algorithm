def solution(numbers):
    answer = 45
    num = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in num:
            answer -= i
    return answer