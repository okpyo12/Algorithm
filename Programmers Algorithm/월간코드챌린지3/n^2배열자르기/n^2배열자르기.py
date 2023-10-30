def solution(n, left, right):
    col = (left) // n
    row = left % n
    arr = []
    for i in range(left, right+1, 1):
        col = (i) // n
        row = i % n
        if col >= row:
            arr.append(col+1)
        else:
            arr.append(row + 1)
    return arr