def solution(nums):
    num = set(nums)
    if len(num) > len(nums)//2:
        return len(nums)//2
    else:
        return len(num)