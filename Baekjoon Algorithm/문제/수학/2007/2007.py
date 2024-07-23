import sys

input = sys.stdin.readline

x, y = map(int, input().split())

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = 0

for i in range(x-1):
    total += month[i]

total += y
total %= 7

print(week[total])