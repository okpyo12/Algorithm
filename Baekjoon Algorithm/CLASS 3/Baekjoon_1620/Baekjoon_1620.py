import sys

N, M = map(int, sys.stdin.readline().split())

dogam = dict()

for i in range(N):
    pokemon = sys.stdin.readline()
    dogam[pokemon[:-1]] = str(i+1)

dogam2 = {v:k for k,v in dogam.items()}
for i in range(M):
    result = sys.stdin.readline()
    if result[:-1] in dogam:
        print(dogam[result[:-1]])
    else:
        print(dogam2[result[:-1]])
