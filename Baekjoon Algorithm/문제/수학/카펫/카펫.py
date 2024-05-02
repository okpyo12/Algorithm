def solution(brown, yellow):
    answer = []
    x = (brown + 4) // 2
    
    for i in range(1, x):
        if i * (x-i) - brown == yellow:
            answer = [i, x-i]
    return answer