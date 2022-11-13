# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        
        while (low <= high):
            mid = (low + high) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                if isBadVersion(mid - 1) == False:
                    return mid
                else:
                    high = mid - 1
        
        return n
            