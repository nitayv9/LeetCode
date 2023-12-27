from functools import lru_cache
#https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#Recursive Solution

def numRollsToTarget(n, k, target) :
    mod = 1000000007
    @lru_cache(None)
    def dm(remain_cubes, total_left):
        if total_left < 1 or remain_cubes == 0:
            return 0
        elif remain_cubes == 1 and total_left < k + 1:
            return 1
        else:
            s = 0
            for i in range(1, k + 1):
                s = (s + dm(remain_cubes - 1, total_left - i)) % mod
            return s

    return dm(n, target)

print(numRollsToTarget(2,6,7))