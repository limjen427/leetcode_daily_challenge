class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        import numpy as np
        from math import comb
        s = set(nums)
        nums_arr = np.array(nums)
        same_val_count = []
        for x in s:
            duplicate_count = len(np.where(nums_arr == x)[0])
            same_val_count.append(duplicate_count)
        
        good_pairs = 0
        for c in same_val_count:
            if c != 1:
                good_pairs += comb(c, 2)
        return good_pairs