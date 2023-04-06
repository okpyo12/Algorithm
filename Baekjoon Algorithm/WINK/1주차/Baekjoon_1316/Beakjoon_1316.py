import sys

input = sys.stdin.readline

N = int(input())
cnt = N

for i in range(N):
    arr = []
    word = input()
    for j in range(len(word)-1):
        if word[j] in arr:
            cnt -= 1 
            break
        if word[j] == word[j+1]:
            pass
        else:
            arr.append(word[j])

print(cnt)