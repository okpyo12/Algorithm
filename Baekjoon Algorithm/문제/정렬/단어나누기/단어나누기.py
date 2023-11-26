import sys

input = sys.stdin.readline

word = input().rstrip()

arr = []

for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        temp = []
        temp.append(word[:i])
        temp.append(word[i:j])
        temp.append(word[j:])
        for k in range(len(temp)):
            temp[k] = list(temp[k])
            temp[k].reverse()
            temp[k] = ''.join(temp[k])
        reverse_arr = ''.join(temp)
        arr.append(reverse_arr)

arr.sort()
print(arr[0])