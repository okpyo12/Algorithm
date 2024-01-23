import sys, heapq

abs_heap = []
input = sys.stdin.readline

n = int(input())
for i in range(n):
	num = int(input())
	if num:
		heapq.heappush(abs_heap, (abs(num), num))
	else:
		if abs_heap:
			print(heapq.heappop(abs_heap)[1])
		else:
			print(0)