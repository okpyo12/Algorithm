def solution(sizes):
    a, b = [], []
    for i in sizes:
        a.append(max(i))
        b.append(min(i))
    a.sort()
    b.sort()
    return a[-1]*b[-1]