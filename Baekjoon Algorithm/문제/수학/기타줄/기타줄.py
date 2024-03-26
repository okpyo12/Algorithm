import sys

input = sys.stdin.readline

N, M = map(int, input().split())

result = 0
pack = 99999999
each = 99999999

for i in range(M):
    a, b = map(int, input().split())
    pack = min(pack, a)
    each = min(each, b)

if each * 6 <= pack:
    result = each * N
else:
    if N < 6:
        result = min(each * N, pack)
    else:
        result = (N // 6) * pack + min((N % 6) * each, pack)
        
print(result)