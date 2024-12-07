class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i] #[1,1,2,2] BECOMES [1,2,2,2] and so on.
                j+=1
        return j

