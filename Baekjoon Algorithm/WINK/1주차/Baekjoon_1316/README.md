# [분수찾기](https://www.acmicpc.net/problem/1193)

<div align = center>

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞은 사람 | 정답 비율 |
| :-------: | :---------: | :---: | :---: | :-------: | :-------: |
|  0.5 초   |   256 MB    | 99409 | 49665 |   42820   |  51.176%  |

</div>

### 문제

무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

| 1/1 | 1/2 | 1/3 | 1/4 | 1/5 | ... | </br>
| 2/1 | 2/2 | 2/3 | 2/4 |... | ... | </br>
| 3/1 | 3/2 | 3/3 | ... | ... | ... | </br>
| 4/1 | 4/2 | ... | ... | ... | ... | </br>
| 5/1 | ... | ... | ... | ... | ... | </br>
| ... | ... | ... | ... | ... | ... |

이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

---

### 출력

첫째 줄에 분수를 출력한다.

---

### 예제 입력

| 예제 입력1 | 예제 출력1 |
| :--------: | :--------: |
|     1      |    1/1     |

| 예제 입력2 | 예제 출력2 |
| :--------: | :--------: |
|     2      |    1/2     |

| 예제 입력3 | 예제 출력3 |
| :--------: | :--------: |
|     3      |    2/1     |

| 예제 입력4 | 예제 출력4 |
| :--------: | :--------: |
|     4      |    3/1     |

| 예제 입력5 | 예제 출력5 |
| :--------: | :--------: |
|     5      |    2/2     |

| 예제 입력6 | 예제 출력6 |
| :--------: | :--------: |
|     6      |    1/3     |

| 예제 입력7 | 예제 출력7 |
| :--------: | :--------: |
|     7      |    1/4     |

| 예제 입력8 | 예제 출력8 |
| :--------: | :--------: |
|     8      |    2/3     |

| 예제 입력9 | 예제 출력9 |
| :--------: | :--------: |
|     9      |    3/2     |

| 예제 입력10 | 예제 출력10 |
| :---------: | :---------: |
|     14      |     2/4     |
