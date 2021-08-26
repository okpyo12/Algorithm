N = int(input())

room = 0
sum_num = 1
num = 0

while N > sum_num:
    room += 1
    sum_num += room*(num + 6)

print(room+1)