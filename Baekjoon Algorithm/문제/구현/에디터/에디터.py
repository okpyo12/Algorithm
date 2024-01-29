import sys

input = sys.stdin.readline

arr1 = list(sys.stdin.readline().rstrip())
arr2 = []
M = int(input())

for _ in range(M):
	command = list(sys.stdin.readline().split())
	if command[0] == 'L':
		if arr1:
			arr2.append(arr1.pop())
            
	elif command[0] == 'D':
		if arr2:
			arr1.append(arr2.pop())

	elif command[0] == 'B':
		if arr1:
			arr1.pop()
            
	else:
		arr1.append(command[1])
        
arr1.extend(reversed(arr2))
print(''.join(arr1))