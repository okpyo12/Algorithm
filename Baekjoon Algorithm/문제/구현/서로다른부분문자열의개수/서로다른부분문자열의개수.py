import sys

input = sys.stdin.readline

S = input().rstrip()

num = 0
result = set()

for i in range(len(S),0,-1):
    num += 1 
    for j in range(i):
        if S[j:j+num] not in result:
            result.add(S[j:j+num])
print(len(result))