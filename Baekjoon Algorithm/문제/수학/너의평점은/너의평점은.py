import sys

input = sys.stdin.readline

grade = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F':0}

total = 0
number = 0

for i in range(20):
    A, B, C = input().split()
    if C != 'P':
        total += (float(B)*(float(grade[C])))
        number += 1*float(B)

if number != 0:
    print(round(total/number,6))
else:
    print(0)