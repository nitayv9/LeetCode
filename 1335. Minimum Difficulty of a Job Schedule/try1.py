#DP
#dp[i][j] represents the sub problem - min difficulty for jobs i...n with j days. looking for dp[0][d]
#k represents the next cut we take from i to k to the next day.

def minDifficulty(jobDifficulty, d):
    if len(jobDifficulty) < d:
        return -1
    dp = [[float('inf')] * (d + 1) for _ in range(len(jobDifficulty) + 1)]
    dp[-1][0] = 0
    for i in range(len(jobDifficulty) - 1 ,-1,-1):
        for j in range(1, d+1):
            for k in range(i , len(jobDifficulty)):
                dp[i][j] = min(dp[i][j], max(jobDifficulty[i:k + 1]) + dp[k+1][j-1])
    return dp[0][d]
