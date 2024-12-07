def searchInsertPoint(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_point = left + (right - left) // 2

        if nums[mid_point] == target:
            return mid_point

        elif nums[mid_point] < target:
            left = mid_point + 1

        else:
            right = mid_point - 1

    return left

result = searchInsertPoint([1, 2, 6, 7], 5)
print(result)  # Output: 2
