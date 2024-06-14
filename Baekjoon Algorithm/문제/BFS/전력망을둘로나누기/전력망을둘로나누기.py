from collections import deque

def bfs(arr, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        cnt += 1
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt


def solution(n, wires):
    answer = n - 2
    for i in range(len(wires)):
        temp = wires.copy()
        arr = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        temp.pop(i)
        for wire in temp:
            x, y = wire
            arr[x].append(y)
            arr[y].append(x)
        for idx,g in enumerate(arr):
            if g != []:
                start = idx
                break
        cnts = bfs(arr, start, visited)
        other_cnts = n - cnts
        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)
    return answer