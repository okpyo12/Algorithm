S = input()

alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr = []
for i in range(26):
    arr.append(-1)

for i in range(len(S)):
    for j in range(26):
        if S[i] == alpabet[j]:
            if arr[j] == -1:
                arr[j] = i

for i in range(26):
    print(arr[i], end=' ')