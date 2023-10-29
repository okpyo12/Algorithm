import itertools

def solution(nums):
    answer = 0
    nCr = list(itertools.combinations(nums, 3))
    for i in nCr:
        if isPrime(sum(i)):
            answer += 1
    return answer

def isPrime(num):
    for i in range(2, num-1, 1):
        if num % i == 0:
            return 0
    return 1