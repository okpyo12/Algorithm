# [완주하지못한선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3)

<div align = center>

| 시간 제한 | 메모리 제한 |  제출  | 정답  | 맞은 사람 | 정답 비율 |
| :-------: | :---------: | :----: | :---: | :-------: | :-------: |
|   2 초    |   256 MB    | 112500 | 27941 |   19713   |  23.279%  |

</div>

### 문제

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

---

### 입력

마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

---

### 출력

---

### 예제 입력

participant completion return <br/>
["leo", "kiki", "eden"] ["eden", "kiki"] "leo" <br/>
["marina", "josipa", "nikola", "vinko", "filipa"] ["josipa", "filipa", "marina", "nikola"] "vinko" <br/>
["mislav", "stanko", "mislav", "ana"] ["stanko", "ana", "mislav"] "mislav"
