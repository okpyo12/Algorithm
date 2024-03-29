# [친구](https://www.acmicpc.net/problem/1058)

<div align = center>

| 시간 제한 | 메모리 제한 | 제출  | 정답 | 맞은 사람 | 정답 비율 |
| :-------: | :---------: | :---: | :--: | :-------: | :-------: |
|   2 초    |   128 MB    | 10558 | 4766 |   3960    |  46.539%  |

</div>

### 문제

지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.

A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.

---

### 입력

첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.

---

### 출력

첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.

---

### 예제 입력

|        예제 입력1         | 예제 출력1 |
| :-----------------------: | :--------: |
| 3<br/>NYY<br/>YNY<br/>YYN |     2      |

|        예제 입력2         | 예제 출력2 |
| :-----------------------: | :--------: |
| 3<br/>NNN<br/>NNN<br/>NNN |     0      |

|                     예제 입력3                      | 예제 출력3 |
| :-------------------------------------------------: | :--------: |
| 5<br/>NYNNN<br/>YNYNN<br/>NYNYN<br/>NNYNY<br/>NNNYN |     4      |

|                                                                        예제 입력4                                                                        | 예제 출력4 |
| :------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------: |
| 10<br/>NNNNYNNNNN<br/>NNNNYNYYNN<br/>NNNYYYNNNN<br/>NNYNNNNNNN<br/>YYYNNNNNNY<br/>NNYNNNNNYN<br/>NYNNNNNYNN<br/>NYNNNNYNNN<br/>NNNNNYNNNN<br/>NNNNYNNNNN |     8      |
