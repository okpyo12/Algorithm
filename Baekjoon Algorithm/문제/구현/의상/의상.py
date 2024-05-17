def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = [i[0]]
        else:
            dic[i[1]].append(i[0])
    result = 1
    print(len(dic))
    if len(dic) >= 2:
        for i in dic:
            result *= len(dic[i]) + 1
        return result-1
    else:
        for i in dic:
            return len(dic[i])
    print(dic)