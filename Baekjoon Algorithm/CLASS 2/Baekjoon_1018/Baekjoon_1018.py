N, M = map(int, input().split())

arr = []
for i in range(N):
    board = input()
    arr.append(board)
checklist1 = ['WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW']

checklist2 = ['BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB',
              'BWBWBWBW',
              'WBWBWBWB']

result = 0
result_arr = []
for i in range(N-7):
    for j in range(M-7):
        for k in range(8):
            for z in range(8):
                if arr[k+i][z+j] == checklist1[k][z]:
                    continue
                else:
                    result += 1
        result_arr.append(result)
        result = 0
        for k in range(8):
            for z in range(8):
                if arr[k+i][z+j] == checklist2[k][z]:
                    continue
                else:
                    result += 1
        result_arr.append(result)
        result = 0

result_arr.sort()
print(result_arr[0])