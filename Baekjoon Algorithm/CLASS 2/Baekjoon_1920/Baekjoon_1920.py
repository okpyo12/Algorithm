N = int(input())
result = []
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()

def binarysearch(arr, x):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low+high)//2
        if x == arr[mid]:
            print(1)
            return True
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid -1
    print(0)
    return 0

for i in range(M):
    binarysearch(arr1, arr2[i])