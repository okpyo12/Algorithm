from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    def dungeon(k, arr):
        cnt = 0
        for i in arr:
            if i[0] <= k:
                k -= i[1]
                cnt += 1
        return cnt
    
    for i, perm in enumerate(permutations(dungeons, len(dungeons))):
        answer = max(answer, dungeon(k, perm))
    return answer