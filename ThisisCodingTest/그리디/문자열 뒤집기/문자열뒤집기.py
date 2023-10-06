import sys

input = sys.stdin.readline

S = input().rstrip()

result = 0

if S[0] == 0:
    for i in range(len(S)):
        if S[i] == "1":
            result += 1
            if S[i-1] == "1":
                result -= 1            
else:
    for i in range(len(S)):
        if S[i] == "0":
            result += 1
            if S[i-1] == "0":
                result -= 1

print(result)