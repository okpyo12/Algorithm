# 팩토리얼 계산(Factorial)

다음 점화식(recursive equation)을 이용하여 팩토리얼을 계산하는 재귀함수를 구현하시오.

단, 그 값은 마지막에 나타나는 연속적인 모든 0을 제외한 마지막 세자리만 출력한다. 예를 들 어 10!인 경우에는 그 값이
10! = 3628800
이므로 288 을 출력한다.

## 입력

입력은 표준입력(standard input)을 사용한다. 입력은 𝑡개의 테스트 케이스로 주어진다. 입력의 첫 번째 줄에 테스트 케이스의 개수를 나타내는 정수 𝑡가 주어진다. 두 번째 줄부터 𝑡개의 줄에 는 한 줄에 한 개의 테스트 케이스에 해당하는 정수 𝑛(0≤𝑛≤ 1,000)이 주어진다. 잘못된 데이 터가 입력되는 경우는 없다.

## 출력

출력은 표준출력(standard output)을 사용한다. 입력되는 테스트 케이스의 순서대로 다음 줄에 이어서 각 테스트 케이스의 결과를 출력한다. 각 테스트 케이스의 출력되는 첫 줄에 입력으로 주 어진 정수 𝑛에 대한 𝑛!를 출력하되, 마지막에 나타나는 연속적인 모든 0을 제외한 마지막 세자 리만 출력한다.

## 입력과 출력의 예

|             입력             |         출력          |
| :--------------------------: | :-------------------: |
| 3 <br/> 0 <br/> 9 <br/> 1000 | 1 <br/> 288 <br/> 472 |
