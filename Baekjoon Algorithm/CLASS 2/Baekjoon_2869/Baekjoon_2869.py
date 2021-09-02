import math
A, B, V = map(int, input().split())

num = A - B
print(math.ceil((V-B)/num))