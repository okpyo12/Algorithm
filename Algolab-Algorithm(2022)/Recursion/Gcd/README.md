# 유클리드 알고리즘(GCD)

두 개의 음수가 아닌 정수 𝑎,𝑏에 대하여, 𝑎와 𝑏를 나누는 자연수 중에서 가장 큰 자연수를 𝑎와 𝑏의 최대공약수(greatest common divisor, gcd)라고 하고 gcd(𝑎,𝑏)로 표시한다. 예를 들어, 132 과 36 의 최대공약수는 gcd(132, 36) = 12 이다.
주어진 두 자연수의 최대공약수를 구하는 알고리즘 중에서 가장 유명한 알고리즘은 유클리드 알 고리즘(Euclid's algorithm)으로서 다음과 같은 최대공약수의 성질을 이용한다.

여기서 mod 는 나머지 연산자(C 언어의 연산자 %와 동일함)를 나타낸다. 이 유클리드 알고리즘을 이용하여 36 과 132 의 최대공약수를 구하면 다음과 같다
gcd(132, 36) = gcd(36, 24)
= gcd(24, 12)
= gcd(12, 0) = 12
두 개의 음이 아닌 정수가 주어졌을 때, 두 정수의 최대공약수를 유클리드 알고리즘으로 계산하 는 프로그램을 작성하시오.

## 입력

입력은 표준입력(standard input)을 사용한다. 입력은 𝑡 개의 테스트 케이스로 주어진다. 입력의 첫 번째 줄에 테스트 케이스의 개수를 나타내는 정수 𝑡가 주어진다. 두 번째 줄부터 𝑡 개의 줄에 는 한 줄에 한 개의 테스트 케이스에 해당하는 두 개의 음이 아닌 정수 𝑎𝑏(0≤𝑎,𝑏≤1,000,000) 가 주어진다. 두 정수 사이에는 한 개의 공백이 있으며, 잘못된 데이터가 입력되는 경우는 없다.

## 출력

출력은 표준출력(standard output)을 사용한다. 입력되는 테스트 케이스의 순서대로 다음 줄에 이어서 각 테스트 케이스의 결과를 출력한다. 각 테스트 케이스의 출력되는 첫 줄에 입력으로 주 어진 두 정수의 최대공약수를 출력한다.

## 입력과 출력의 예

|              입력               |        출력         |
| :-----------------------------: | :-----------------: |
| 3<br/>132 36<br/>0 12<br/>132 1 | 12 <br/> 12 <br/> 1 |
