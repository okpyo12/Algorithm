import sys

input = sys.stdin.readline

N = int(input())

S = []
for _ in range(N):
    cal = input().rstrip()
    if cal != "all" and cal != "empty":
        action, num = cal.split()
        num = int(num)
    else:
        action = cal
    if action == "add":
        if num not in S:
            S.append(num)
    elif action == "remove":
        if num in S:
            S.remove(num)
    elif action == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif action == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.append(num)
    elif action == "all":
        S = [i for i in range(1, 21)]
    elif action == "empty":
        S = []
