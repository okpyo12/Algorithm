N = input()
list = []
list = input().split()
total = 0

N = int(N)
max_num = int(list[0])

for i in range(N-1):
    if max_num < int(list[i+1]):
        max_num = int(list[i+1])

for i in range(N):
    list[i] = int(list[i])/max_num*100


for i in range(N):
    total += list[i]

result = total/N
print(result)