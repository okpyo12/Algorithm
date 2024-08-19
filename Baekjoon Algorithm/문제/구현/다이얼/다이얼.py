import sys

input = sys.stdin.readline

LS_dict = {"ABC":3,"DEF":4,"GHI":5,"JKL":6, "MNO":7, "PQRS":8, "TUV":9, "WXYZ":10}

S = input()
time = 0

for s in S:
    for k,v in LS_dict.items():
        if s in k:
            time += v

print(time)