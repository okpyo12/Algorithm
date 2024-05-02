def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    startTime = h1 * 3600 + m1 * 60 + s1
    endTime = h2 * 3600 + m2 * 60 + s2  

    if startTime == 0 * 3600 or startTime == 12 * 3600:
        answer += 1

    while startTime < endTime:
        hCurAngle = startTime / 120 % 360
        mCurAngle = startTime / 10 % 360
        sCurAngle = startTime * 6 % 360

        hNextAngle = 360 if (startTime + 1) / 120 % 360 == 0 else (startTime + 1) / 120 % 360
        mNextAngle = 360 if (startTime + 1) / 10 % 360 == 0 else (startTime + 1) / 10 % 360
        sNextAngle = 360 if (startTime + 1) * 6 % 360 == 0 else (startTime + 1) * 6 % 360

        if sCurAngle < hCurAngle and sNextAngle >= hNextAngle:
            answer += 1
        if sCurAngle < mCurAngle and sNextAngle >= mNextAngle:
            answer += 1
        
        if sNextAngle == hNextAngle and hNextAngle == mNextAngle:
            answer -= 1

        startTime += 1
    
    return answer

# print(solution(0, 5, 30, 0, 7, 0))
print(solution(12, 0, 0, 12, 0, 30))
# print(solution(1, 5, 5, 1, 5, 6))
# print(solution(0, 6, 1, 0, 6, 6))
# print(solution(11, 58, 59, 11, 59, 0))
# print(solution(11, 59, 30, 12, 0, 0))
# print(solution(0, 0, 0, 23, 59, 59))