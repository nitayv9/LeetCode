from functools import lru_cache

# Try one. not good enough. calculate j everytime might be too expensive. make it O(n^2) worst case.


def minCost(colors, neededTime):

    @lru_cache(None)
    def recursive_dp(n):
        if n == -1 or n == 0:
            return 0
        else:
            if colors[n] != colors[n-1]:
                return recursive_dp(n-1)

            opt1 = recursive_dp(n - 1) + neededTime[n]  # removing last ballon
            j = n - 2 # let j be the last index that its color differnt than n
            times = neededTime[j + 1]
            while j != -1 and colors[j] == colors[n]:
                j = j - 1
                times = times + neededTime[j + 1]
            opt2 = recursive_dp(j) + times
            return min(opt1, opt2)

    return recursive_dp(len(colors) - 1)


colors_inputs = ["abaac", "abc", "aabaa"]
neededTime_inputs = [[1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4, 1]]

for colors, neededTime in zip(colors_inputs, neededTime_inputs):
    print(f"Input: colors = {colors}, neededTime = {neededTime}. Output = {minCost(colors,neededTime)}")
