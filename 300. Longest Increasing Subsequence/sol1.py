# https://leetcode.com/problems/longest-increasing-subsequence/submissions/1137865332/?envType=daily-question&envId=2024-01-05
# dp[i] represents the longest subseqence from index i to n-1 with taking the element at dp[i] into the solution.
# Time - O(n^2)

def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    currMax = 1
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
        currMax = max(currMax, dp[i])
    return currMax
