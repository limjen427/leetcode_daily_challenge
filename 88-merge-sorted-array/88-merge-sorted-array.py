class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        """
        check = len(nums1)-1   #total nums1 array length
        m -= 1  #nums1 number check point
        n -= 1  #nums2 number check point
        
        while m >= 0 and n >= 0:    #until it both array check whole number
            if nums1[m] >= nums2[n]: #nums1 > nums2
                nums1[check] = nums1[m] #nums1 put it at very end
                m -= 1
            else :                   #nums1 < nums2
                nums1[check] = nums2[n] #nums2 put it at very end
                n -= 1
                
            check -= 1
            
        if n >= 0:      #if nums1 still have number left
            nums1[:n+1] = nums2[:n+1] #beginning to n+1
        
        """
        
        
        """
        check = 0
        x = 0
        temp = 0
        
        for x in range(0, (m+n)):
            if nums1[x] >= nums2[check] :
                temp = nums1[x]
                nums1[x] = nums2[check]
                nums1[x + 1] = temp
                check += 1
            if nums1[x] == 0:
                nums1[x] = nums2[check]
                check += 1
        """
        #"""
        i, j, check = m-1, n-1, len(nums1)-1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[check] = nums1[i]
                i -= 1
            else:
                nums1[check] = nums2[j]
                j -= 1
            check -= 1
        #"""
        
        
