import bisect

def jobScheduling(startTime, endTime, profit):
    n = len(startTime)
    data = [(0, 0, 0)] + list(zip(startTime, endTime, profit))
    data.sort(key=lambda a: a[1])
    dp = [0] * (n + 1)
    for j in range(1, n + 1):
        lastActivityendsbeforej = bisect.bisect_right(data, data[j][0], lo=0, hi=j, key=lambda a: a[1]) - 1
        dp[j] = max(dp[j - 1], data[j][2] + dp[lastActivityendsbeforej])
    return dp[-1]
