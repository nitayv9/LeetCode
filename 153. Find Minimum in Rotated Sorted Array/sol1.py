
def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[right] < nums[middle]:
            left = middle + 1
        else:
            right = middle

    return nums[left]


arr = [1,2,3,4,5,7,8,0]
print(findMin(arr))
