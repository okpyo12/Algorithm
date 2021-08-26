A, B = map(int, input().split())

arr_A = []
arr_B = []
result = []
for i in range(1, A+1):
    if A % i == 0:
        arr_A.append(i)

for i in range(1, B+1):
    if B % i == 0:
        arr_B.append(i)

arr = list(set(arr_A) & set(arr_B))
arr.sort()
print(arr[-1])
print(A*B//arr[-1])