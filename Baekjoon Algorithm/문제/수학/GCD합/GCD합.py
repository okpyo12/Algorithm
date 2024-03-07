import sys
from itertools import combinations
import math

input = sys.stdin.readline

t = int(input())

def get_gcd(a, b): # while문을 활용한 유클리드 호제법 구현
	while b : 
		a, b = b, a % b
	return a


for i in range(t):
    answer = 0
    arr = list(map(int, input().split()))
    del arr[0]
    combs = combinations(arr, 2)
    for comb in combs:
        a, b = comb
        answer += math.gcd(a, b)
    print(answer)
