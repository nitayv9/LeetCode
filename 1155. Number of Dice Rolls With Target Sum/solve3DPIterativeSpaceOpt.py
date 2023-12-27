from collections import defaultdict
# iterative memo Solution, optimize Space Complexity

def numRollsToTarget(n, k, target) :
    mod = 1000000007
    pev = [0 for _ in range(target + 1)]
    nex = [0 for _ in range(target + 1)]

    for i in range(1, k + 1):
        pev[i] = 1
    for remainCubes in range(2, n + 1):
        for targ in range(1, target + 1):
            s = 0
            for i in range(1, k + 1):
                if target - i > 0:
                    s = (s + pev[targ - i]) % mod
            nex[targ] = s
        pev = nex.copy()

    return nex[target]





print(numRollsToTarget(30,30,500))