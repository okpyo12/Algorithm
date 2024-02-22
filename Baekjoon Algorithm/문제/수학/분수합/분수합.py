import sys
import math

input = sys.stdin.readline

A_num1, B_num1 = map(int, input().split())
A_num2, B_num2 = map(int, input().split())

A_num = (A_num1 * B_num2)+ (A_num2 * B_num1)
B_num = B_num1 * B_num2

for i in range(int(math.sqrt(B_num))+1, 1, -1):
    if B_num % i == 0 and A_num % i == 0:
        A_num = A_num // i
        B_num = B_num // i

print(A_num, B_num)