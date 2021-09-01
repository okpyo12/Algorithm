N = int(input())

five_kg = N//5
three_kg = N//3
result = -1
for i in range(five_kg+1):
    for j in range(three_kg+1):
        a = i*5 + j*3
        if a == N:
            result = i + j
            break
print(result)