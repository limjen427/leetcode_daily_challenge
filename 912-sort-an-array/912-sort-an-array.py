class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums)
        return nums
    
    
    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            l = nums[:mid]
            r = nums[mid:]
            self.merge_sort(l)
            self.merge_sort(r)
 
            i = j = 0
            m = 0

            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    nums[m] = l[i]
                    i += 1
                else:
                    nums[m] = r[j]
                    j += 1
                m += 1

            # Checking if any element was left
            while i < len(l):
                nums[m] = l[i]
                i += 1
                m += 1

            while j < len(r):
                nums[m] = r[j]
                j += 1
                m += 1