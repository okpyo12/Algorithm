import sys

input = sys.stdin.readline

T = int(input())

def dfs(x): #DFS 함수 정의
    visited[x] = True #방문 체크
    number = numbers[x] #다음 방문 장소
    if not visited[number]: #방문하지 않았다면
        dfs(number) #재귀

for _ in range(T):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문여부확인용
    result = 0
    
    for i in range(1, N+1):
        if not visited[i]: #방문하지 않았다면
            dfs(i) #DFS실행
            result += 1 #결과값 += 1
    print(result)