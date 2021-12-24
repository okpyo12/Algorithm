def solution(n, m):
    for i in range(n):
        if n%(n-i)+m%(n-i) == 0:
            return [n-i, n*m/(n-i)]
n = 16
m = 12
print(solution(n, m))
