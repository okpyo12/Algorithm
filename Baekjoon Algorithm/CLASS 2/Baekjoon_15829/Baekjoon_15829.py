import sys

L = int(sys.stdin.readline())
a = input()
r = 31
M = 1234567891

alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
            'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

result = 0
cnt = 0
for i in a:
    result += alphabet[i]*(r**cnt)
    cnt += 1
print(result%M)