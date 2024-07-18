import sys 

input = sys.stdin.readline

N, M = map(int, input().split())

result = 0

if N == 1:
  result = 1

elif N == 2: 
  if M >= 1 and M <= 6:
    result = (M + 1) // 2 
  elif M >= 7:
    result = 4
elif N >= 3: 
  if M <= 6:
    result = min(M, 4)
  elif M >= 7:
    result = M - 2
print(result)