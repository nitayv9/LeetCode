
#dp[i,j] represents the number of arithmetic subsequences that ends with indexes i,j.
#Time Complexity - O(n^3)

def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [[0] * n for i in range(n)]
    total_subsequences = 0
    for i in range(1,n):
        for j in range(i+1,n):
            diff = nums[j] - nums[i]
            for k in range(0,i):
                if nums[i] - nums[k] == diff:
                    dp[i][j] = dp[i][j] + 1 + dp[k][i]
                    # + 1 stands for the new subsequence [k,i,j].
                    # and pd[k][i] for each subsequence finished with k,i we count another one ends with j. [..,k,i,j]
            total_subsequences = total_subsequences + dp[i][j]
    return total_subsequences
