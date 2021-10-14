import sys

N, M = map(int, sys.stdin.readline().split())
arr1, arr2 = [], []
for i in range(N):
    arr1.append(sys.stdin.readline().rstrip())
for i in range(M):
    arr2.append(sys.stdin.readline().rstrip())
    
result = list(set(arr1) & set(arr2))
sorted_result = sorted(result)
print(len(result))
for i in sorted_result:
    print(i)