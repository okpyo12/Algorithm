import math

def solution(fees, records):
    answer = []
    dic = {}
    arr = []
    for i in records:
        time, carnum, inout = i.split()
        carnum = int(carnum)
        nh, nm = map(int, time.split(':'))
        if inout == 'IN':
            arr.append([nh, nm, carnum])
            if carnum not in dic:
                dic[carnum] = 0
        else:
            for j in range(len(arr)):
                if arr[j][2] == carnum:
                    if nm - arr[j][1] >= 0:
                        parktime = (nh - arr[j][0])*60 + (nm - arr[j][1])
                    else:
                        parktime =  (nh - arr[j][0] - 1)*60 + (nm - arr[j][1] + 60)
                    del arr[j]
                    dic[carnum] += parktime
                    break
    if arr != []:
        for i in arr:
            parktime = (23 - i[0])*60 + (59 - i[1])
            dic[i[2]] += parktime

    for i in dic:
        if dic[i] > fees[0]:
            dic[i] = fees[1] + (math.ceil((dic[i] - fees[0]) / fees[2]) * fees[3])
        else:
            dic[i] = fees[1]
    dic = sorted(dic.items(), key=lambda x : x)
    for i in dic:
        answer.append(i[1])

    return answer

# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
# print(solution([1, 461, 1, 10],["00:00 1234 IN"]))
print(solution([180, 5000, 10, 1000],["05:59 0000 IN", "05:59 1111 IN"]))