class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row check?
        low_r = 0
        high_r = len(matrix) - 1
        # low = matrix[0][0]
        # high = matrix[len(matrix)-1][0]
        while (low_r <= high_r):
            mid = (low_r + high_r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high_r = mid - 1
            else:
                low_r = mid + 1
        
        #use high_r as row value
        low_c = 0
        high_c = len(matrix[high_r]) - 1
        
        while (low_c <= high_c):
            mid = (low_c + high_c) // 2
            if matrix[high_r][mid] == target:
                return True
            elif matrix[high_r][mid] > target:
                high_c = mid - 1
            else:
                low_c = mid + 1
        
        return False
            
        
        #column check?