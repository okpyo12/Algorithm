# 1로 만들기

<div align = center>

| 시간 제한 | 메모리 제한 |
| :-------: | :---------: |
|   1 초    |   128 MB    |

</div>

### 문제

정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.

X가 5로 나누어떨어지면, 5로 나눈다.
X가 3으로 나누어떨어지면, 3으로 나눈다.
X가 2로 나누어떨어지면, 2로 나눈다.
X에서 1을 뺀다.
정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값이다.

1. 26 - 1 = 25 (4)
2. 25 / 5 = 5 (1)
3. 5 / 5 = 1 (1)

### 입력 조건

첫째 줄에 정수 X가 주어진다. (1 <= X <= 30,000)

---

### 출력 조건

첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

---

### 예제 입력

| 예제 입력1 | 예제 출력1 |
| :--------: | :--------: |
|     26     |     3      |
