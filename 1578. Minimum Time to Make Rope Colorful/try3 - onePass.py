#https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

#fact - when we have same color baloon sequence, all must be reomove but one. we need to choose the maximum to remain.
#Time = O(n)
#Space = O(1)
def minCost(colors, neededTime):
    n = len(colors)
    total = 0
    i = 0
    while i < n:
        curMax = neededTime[i]
        total_sum = neededTime[i]
        j = i + 1
        while j < n and colors[i] == colors[j]:
            curMax = max(curMax, neededTime[j])
            total_sum = total_sum + neededTime[j]
            j = j + 1
        if total_sum != neededTime[i]:
            total = total + total_sum - curMax

        i = j
    return total

colors_inputs = ["abaac", "abc", "aabaa", "aaaaa"]
neededTime_inputs = [[1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4, 1],[1, 2, 3, 4, 5]]

for colors, neededTime in zip(colors_inputs, neededTime_inputs):
    print(f"Input: colors = {colors}, neededTime = {neededTime}. Output = {minCost(colors,neededTime)}")


