import sys

input = sys.stdin.readline

king, rock, N = input().split()
king_arr = [ord(king[0])-64, int(king[1])]
rock_arr = [ord(rock[0])-64, int(rock[1])]
arr = []
move = {'R': [1,0], 'L': [-1,0], 'B': [0,-1], 'T': [0,1], 'RT': [1,1], 'LT': [-1,1], 'RB': [1,-1], 'LB': [-1,-1]}

for i in range(int(N)):
    arr.append(input().rstrip())

for i in arr:
    x, y = move[i]
    if 1 <= king_arr[0] + x <= 8 and 1 <= king_arr[1] + y <= 8:
        king_arr[0] = king_arr[0] + x
        king_arr[1] = king_arr[1] + y
        if king_arr == rock_arr:
            if 1 <= rock_arr[0] + x <= 8 and 1 <= rock_arr[1] + y <= 8:
                rock_arr[0] = rock_arr[0] + x
                rock_arr[1] = rock_arr[1] + y
            else:
                king_arr[0] = king_arr[0] - x
                king_arr[1] = king_arr[1] - y

print(chr(king_arr[0]+64), end='')
print(king_arr[1])
print(chr(rock_arr[0]+64), end='')
print(rock_arr[1])