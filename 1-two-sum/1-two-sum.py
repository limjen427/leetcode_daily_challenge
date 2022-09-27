class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_sum = {}
        for i, num in enumerate(nums):
            if target - num in num_sum:
                return [num_sum[target - num], i]
            else:
                num_sum[num] = i
        #return num_sum