# [어린 동물 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/59037)

### 문제 설명

ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

NAME TYPE NULLABLE
ANIMAL_ID VARCHAR(N) FALSE
ANIMAL_TYPE VARCHAR(N) FALSE
DATETIME DATETIME FALSE
INTAKE_CONDITION VARCHAR(N) FALSE
NAME VARCHAR(N) TRUE
SEX_UPON_INTAKE VARCHAR(N) FALSE

---

### 문제

동물 보호소에 들어온 동물 중 젊은 동물1의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.

---

### 예시

이 중 젊은 동물은 Diablo, Miller, Cherokee입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

ANIMAL_ID	NAME
A365172	Diablo
A367012	Miller
A381217	Cherokee

---

### 정답

select ANIMAL_ID, NAME
from ANIMAL_INS
where INTAKE_CONDITION != 'Aged'
order by ANIMAL_ID