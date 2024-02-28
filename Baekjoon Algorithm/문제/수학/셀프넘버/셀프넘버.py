arr = []
for i in range(1,10000):
    al = str(i)
    num = i
    for j in al:
        num += int(j)
    arr.append(num)

for i in range(1,10000):
    if i not in arr:
        print(i)