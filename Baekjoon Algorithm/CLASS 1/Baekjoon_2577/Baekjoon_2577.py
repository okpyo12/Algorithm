A = input()
B = input()
C = input()

num = int(A) *int(B) * int(C)
strnum = str(num)

for i in range(10):
    cnt = 0
    for j in range(len(strnum)):
        if int(strnum[j]) == int(i):
            cnt += 1
    print(cnt)