N = int(input())

num = 0
while True:
    if '666' in str(num):
        N -= 1
        if N == 0:
            print(num)
            break
    num += 1