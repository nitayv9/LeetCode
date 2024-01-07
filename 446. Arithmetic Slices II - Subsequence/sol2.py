from collections import defaultdict
# Like sol1 but instead of running all the indexes from 0  to i we keep it tracked with hash table.
# diff_track[(i,diff)] contains all the indexes <i so the diff from nums[i] is diff.


def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    diff_track = defaultdict(list)
    for i in range(1, n):
        diff_track[(i, nums[i] - nums[0])].append(0)
    total_subsequences = 0
    for i in range(1, n):
        for j in range(i+1, n):
            diff = nums[j] - nums[i]
            diff_track[(j, diff)].append(i)
            same_different = diff_track[(i, diff)]
            for k in same_different:
                if nums[i] - nums[k] == diff:
                    dp[i][j] = dp[i][j] + 1 + dp[k][i]
                    # + 1 stands for the new subsequence [k,i,j].
                    # and pd[k][i] for each subsequence finished with k,i we count another one ends with j. [..,k,i,j]
            total_subsequences = total_subsequences + dp[i][j]
    return total_subsequences
