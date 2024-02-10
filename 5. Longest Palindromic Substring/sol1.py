def longestPalindrome(s):
    n = len(s)
    memo = [[-1] * n for i in range(n)]
    for i in range(n - 1):
        memo[i][i] = 1
        if s[i] == s[i + 1]:
            memo[i][i + 1] = 2
    memo[n - 1][n - 1] = 1
    for gap in range(2, n):
        for i in range(0, n - gap):
            if s[i] == s[i + gap] and memo[i + 1][i + gap - 1] != -1:
                memo[i][i + gap] = memo[i + 1][i + gap - 1] + 2
    m = -1
    maxi = 0
    maxj = 0
    for i in range(n):
        for j in range(n):
            if memo[i][j] > m:
                m = memo[i][j]
                maxi = i
                maxj = j
    return s[maxi:maxj + 1]