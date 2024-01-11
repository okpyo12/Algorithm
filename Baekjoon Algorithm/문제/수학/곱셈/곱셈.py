import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def multi (A,B):
  if B == 1:
      return A % C
  else:
      tmp = multi(A, B//2)
      if B % 2 ==0:
          return (tmp * tmp) % C
      else:
          return (tmp  * tmp * A) % C
          
print(multi(A,B))