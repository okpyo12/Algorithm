N = int(input())

arr = []
for i in range(N):
    arr.append(input())
set_arr = ''
set_arr = set(arr)
arr = list(set_arr)

result = []
for i in arr:
    result.append((len(i),i))

sort_arr = sorted(result)

for i, j in sort_arr:
    print(j)