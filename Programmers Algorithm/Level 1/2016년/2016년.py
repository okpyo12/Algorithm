def solution(a, b):
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"] #1월1일이 금요일이므로 7로 나눴을 때 인덱스 1이 금요일로 나오게 배열을 설정
    mon = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31] #각 달의 날짜만큼 배열로 저장
    
    return day[(sum(mon[:a-1]) + b) % 7]
