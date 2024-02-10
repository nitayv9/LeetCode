#DP
#let the dp[i][j] : the substring starts at i index and ends at j is palindrome
#so dp[i][j] = 1 iff s[i]=s[j] and dp[i+1][j-1] is 1 (palindrome)

def countSubstrings(s):
    n = len(s)
    counter = n  # all the single ways.
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        dp[i][i] = 1
        dp[i][i-1] = 1  # kind of help for case that '..bb..' and we wants it be a palindome.(instead of two base cases)
    for jump in range(1, n):
        for i in range(0, n - jump):
            j = i + jump
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = 1
                counter = counter + 1
    return counter




print(countSubstrings("abcbb"))