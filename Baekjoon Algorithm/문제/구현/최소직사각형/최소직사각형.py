def solution(sizes):
    row, col = [], []
    for size in sizes:
        a, b = size[0], size[1]
        row.append(max(a,b))
        col.append(min(a,b))
    answer = max(row) * max(col)
    return answer