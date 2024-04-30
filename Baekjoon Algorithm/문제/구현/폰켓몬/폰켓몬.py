def solution(nums):
    num = len(nums) // 2
    nums = set(nums)
    if len(nums) < num:
        return len(nums)
    else:
        return num