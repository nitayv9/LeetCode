def minFallingPathSum(matrix) :
    n = len(matrix)
    dp = [[None] * n for _ in range(n)]
    for i in range(n):
        dp[n - 1][i] = matrix[n - 1][i]
    for row in range(n - 2, -1, -1):
        for col in range(n):
            left = float('inf')
            right = float('inf')
            mid = dp[row + 1][col]
            if col - 1 > -1:
                left = dp[row + 1][col - 1]
            if col + 1 < n:
                right = dp[row + 1][col + 1]
            dp[row][col] = matrix[row][col] + min(left, right, mid)

    return min(dp[0])