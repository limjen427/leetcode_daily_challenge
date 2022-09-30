class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #if len(nums) == 0:
         #   return nums[0]
            
        res = 0
        for num in nums:
            res ^= num
        
        return res