def solution(line):
    rem = []
    sss = line[0]
    result = ""
    idx = -1
    for i in line:
        idx += 1
        if idx == 0:
            rem.append(i)
            continue
        if i != sss:
            rem.append(i)
            sss = i
        else:
            if rem[idx-1] != "*":
                rem.append("*")
                continue
            idx -= 1
    for i in rem:
        result += i
    return result


print(solution("aabbbbbbbbc"))