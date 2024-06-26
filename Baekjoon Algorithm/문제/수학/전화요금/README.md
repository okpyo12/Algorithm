# [전화요금](https://www.acmicpc.net/problem/3226)

<div align = center>

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| :-------: | :---------: | :--: | :--: | :-------: | :-------: |
|   1 초    |   128 MB    | 1694 | 757  |    668    |  49.118%  |

</div>

### 문제

7:00부터 19:00까지 전화 요금은 1분에 10원이다.

19:00부터 7:00까지 전화 요금은 1분에 5원이다.

상근이가 전화를 건 시간과 통화 시간이 모두 주어졌을 때, 전화 요금을 구하는 프로그램을 작성하시오.

---

### 입력

첫째 줄에 상근이가 건 전화의 수 N이 주어진다. (1 ≤ N ≤ 100)

다음 N개 줄에는 상근이가 건 전화에 대한 정보가 HH:MM DD와 같은 형식으로 주어진다.

HH:MM은 전화를 건 시간이며, DD는 통화 시간이다. DD는 최대 60이며, MM과 DD사이에는 공백이 하나 주어진다.

만약 시나 분이 한자리 숫자라면, 앞에 0이 하나 주어진다.

시간은 00:00부터 23:59까지이다.

---

### 출력

총 전화 요금을 출력한다.

---

### 예제 입력

|         예제 입력1          | 예제 출력1 |
| :-------------------------: | :--------: |
| 2<br/>11:02 11<br/>15:30 01 |    120     |

|                예제 입력2                | 예제 출력2 |
| :--------------------------------------: | :--------: |
| 3<br/>20:05 12<br/>06:45 30<br/>13:08 15 |    435     |

|                             예제 입력3                             | 예제 출력3 |
| :----------------------------------------------------------------: | :--------: |
| 5<br/>00:00 05<br/>06:47 35<br/>11:30 18<br/>18:33 60<br/>23:59 22 |    1035    |
