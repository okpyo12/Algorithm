list = list(map(int,input().split()))

sum = 0
for i in range(len(list)):
    sum += list[i]*list[i]

result = sum%10
print(result)