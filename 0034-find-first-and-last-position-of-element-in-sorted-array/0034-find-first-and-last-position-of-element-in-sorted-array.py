class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(nums, x):
            low = 0
            high = len(nums) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if x > nums[mid]: 
                    low = mid + 1
                else: 
                    high = mid - 1
            return low

        def binarySearchRight(nums, x):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if x >= nums[mid]: 
                    low = mid + 1
                else: 
                    high = mid - 1
            return high

        low = binarySearchLeft(nums, target)
        high = binarySearchRight(nums, target)
        return (low, high) if low <= high else [-1, -1]