
#This is the same solution as try1 but iterative and calcultig all the j's in the begging using two arrays. continutesColors and times.
#https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

# Time complexity - O(n)
# space Complexity = O(n)
# n = len(color) = len(neededTime)

def minCost(colors, neededTime):
    times = [0] * len(colors)
    continuesColors = [0] * len(colors)
    continuesColors[0] = 1
    for i in range(1,len(colors)):
        if colors[i] != colors[i - 1]:
            continuesColors[i] = 1
        else:
            continuesColors[i] = continuesColors[i-1] + 1
    currColor = colors[0]
    times[0] = neededTime[0]
    for i in range(1, len(colors)):
        if currColor == colors[i]:
            times[i] = times[i-1] + neededTime[i]
        else:
            currColor=colors[i]
            times[i] = neededTime[i]

    lastDiff = 0 # pointer to the last index that its color different from lastdiff+1....i-2(inclusive)

    memo = [0] * len(colors)
    if colors[0] == colors[1]:
        memo[1] = min(neededTime[0],neededTime[1])
    for i in range(2, len(colors)):
        if colors[i] != colors[i-1]:
            memo[i] = memo[i-1]
        else:
            opt1 = memo[i-1] + neededTime[i] #removing last baloon
            opt2 = memo[i-1 - continuesColors[i-1]] + times[i - 1] #removing one before the last baloon and all the baloons needed to make this remove.
            memo[i] = min(opt1 , opt2)
        if colors[lastDiff] != colors[i-1]:
            lastDiff = i - 1
        print(lastDiff)

    return memo[-1]

colors_inputs = ["abaac", "abc", "aabaa"]
neededTime_inputs = [[1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4, 1]]

for colors, neededTime in zip(colors_inputs, neededTime_inputs):
    print(f"Input: colors = {colors}, neededTime = {neededTime}. Output = {minCost(colors,neededTime)}")
