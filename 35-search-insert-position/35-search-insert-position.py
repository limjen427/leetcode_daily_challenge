class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums)
        for i in range(len(nums)):
            if (nums[i] == target):
                return i
            elif (target < nums[i]):
                return i
        return end