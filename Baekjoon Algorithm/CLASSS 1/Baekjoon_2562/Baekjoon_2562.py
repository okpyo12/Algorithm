numlist = []

for i in range(9):
    numlist.append(int(input()))

print(max(numlist))
print(int(numlist.index(max(numlist)))+1)