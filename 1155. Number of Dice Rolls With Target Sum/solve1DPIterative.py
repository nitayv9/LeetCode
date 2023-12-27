from collections import defaultdict
#https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#iterative memo Solution

def numRollsToTarget(n, k, target) :
    mod = 1000000007
    memo = defaultdict(int)
    for i in range(1, k + 1):
        memo[(1,i)] = 1
    for remainCubes in range(2, n + 1):
        for targ in range(1, target + 1):
            s = 0
            for i in range(1, k + 1):
                s = (s + memo[(remainCubes - 1, targ - i)]) % mod
            memo[(remainCubes, targ)] = s

    return memo[(n,target)]
