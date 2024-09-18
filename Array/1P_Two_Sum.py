class Solution(object):
  def twoSum(self, nums, target):
    seen = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]  # Return the indices of the two numbers
        seen[number] = index
    return []  # Return an empty list if no pair is found