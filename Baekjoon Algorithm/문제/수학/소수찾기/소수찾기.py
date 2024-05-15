import math
from itertools import permutations
def is_prime(x):
    if x == 0 or x == 1:
        return 0
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    arr = []
    result = []
    for i in numbers:
        arr.append(i)
    for i in range(1, len(arr)+1):
        for combo in permutations(arr, i):
            temp = ''.join(combo)
            result.append(int(temp))
    result = list(set(result))
    for i in result:
        answer += is_prime(int(i))
    return answer

print(solution("121"))