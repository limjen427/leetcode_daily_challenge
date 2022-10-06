class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []        
        for j in range(len(nums)):
            k = 0
            for i in range(len(nums)):
                if nums[j]>nums[i]:
                    k+=1
            res.append(k)
        return res