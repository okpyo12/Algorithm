# [행렬](https://www.acmicpc.net/problem/1080)

<div align = center>

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞은 사람 | 정답 비율 |
| :-------: | :---------: | :---: | :---: | :-------: | :-------: |
|   2 초    |   128 MB    | 24076 | 10296 |   8271    |  42.656%  |

</div>

### 문제

0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

---

### 입력

첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

---

### 출력

첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

---

### 예제 입력

|                        예제 입력1                         | 예제 출력1 |
| :-------------------------------------------------------: | :--------: |
| 3 4<br/>0000<br/>0010<br/>0000<br/>1001<br/>1011<br/>1001 |     2      |

|                     예제 입력2                      | 예제 출력2 |
| :-------------------------------------------------: | :--------: |
| 3 3<br/>111<br/>111<br/>111<br/>000<br/>000<br/>000 |     1      |

|   예제 입력3    | 예제 출력3 |
| :-------------: | :--------: |
| 1 1<br/>1<br/>0 |     -1     |
