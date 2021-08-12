def solution(s, n):
    answer = ''

    small_alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    large_alpabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index = 0
    result = ''
    for i in range(len(s)):
        for j in range(26):
            index = j + n
            if s[i] == small_alpabet[j]:
                if index <= 25:
                    result += small_alpabet[index]
                else:
                    result += small_alpabet[index - 26]
            elif s[i] == large_alpabet[j]:
                if index <= 25:
                    result += large_alpabet[index]
                else:
                    result += large_alpabet[index - 26]
            elif s[i] == ' ':
                result += ' '
                break
            else:
                continue

    for i in range(len(s)):
        answer += result[i]

    return answer