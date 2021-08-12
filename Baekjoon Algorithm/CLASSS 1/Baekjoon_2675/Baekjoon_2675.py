T = int(input())

sumlist = []
result = ""
resultlist = []
for i in range(T):
    R, S = input().split()
    for j in range(len(S)):
        sumlist.append(S[j]*int(R))
    for j in range(len(S)):
        result += sumlist[j]
    resultlist.append(result)
    result = ""
    sumlist = []

for i in range(T):
    print(resultlist[i])