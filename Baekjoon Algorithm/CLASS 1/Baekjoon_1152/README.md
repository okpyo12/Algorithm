# [단어의 개수](https://www.acmicpc.net/problem/1152)

<div align = center>

| 시간 제한 | 메모리 제한 |  제출  |  정답  | 맞은 사람 | 정답 비율 |
| :-------: | :---------: | :----: | :----: | :-------: | :-------: |
|   2 초    |   128 MB    | 176374 | 50987  |  39811    |  29.141%  |

</div>

### 문제

영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 
이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

---

### 입력

첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문자열이 주어진다.
이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 띄어쓰기 한 개로 구분되며,
공백이 연속해서 나오는 경우는 없다. 또한 문자열의 앞과 뒤에는 공백이 있을 수도 있다.

---

### 출력

첫째 줄에 단어의 개수를 출력한다.

---

### 예제 입력

| 예제 입력1 | 예제 출력1 |
| :--------: | :--------: |
|    The Curious Case of Benjamin Button     | 6 |

| 예제 입력2 | 예제 출력2 |
| :--------: | :--------: |
|     Mazatneunde Wae Teullyeoyo    | 3 |

| 예제 입력3 | 예제 출력3 |
| :--------: | :--------: |
|    Teullinika Teullyeotzi      | 2 |