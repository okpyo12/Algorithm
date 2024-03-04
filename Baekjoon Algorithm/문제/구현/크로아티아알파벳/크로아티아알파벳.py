import sys

input = sys.stdin.readline

word = input().rstrip()

cnt = 0

for i in range(len(word)):
    if i == len(word)-1:
        cnt += 1
        break
    
    if word[i+1] == '-' or word[i+1] == '=':
        continue
    if word[i] == 'c':
        if word[i+1] == '-' or word[i+1] == '=':
            continue
        else:
            cnt += 1
    elif word[i] == 'd':
        if i == len(word)-2:
            if word[i+1] == '-':
                continue
            else:
                cnt += 1
        elif i <= len(word)-3:
            if word[i+1] == 'z' and word[i+2] == '=':
                continue
            else:
                cnt += 1
    elif word[i] == 'l':
        if word[i+1] == 'j':
            continue
        else:
            cnt += 1
    elif word[i] == 'n':
        if word[i+1] == 'j':
            continue
        else:
            cnt += 1
    elif word[i] == 's':
        if word[i+1] == '=':
            continue
        else:
            cnt += 1
    elif word[i] == 'z':
        if word[i+1] == '=':
            continue
        else:
            cnt += 1
    else:
        cnt += 1

print(cnt)