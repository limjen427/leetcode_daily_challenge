class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search in each row
        #linear in each column
        
        for r in range(len(matrix)):
            low = 0
            high = len(matrix[r]) - 1
            print(r, low, high)
            
            while (low <= high):
                mid = (low + high) // 2
                if matrix[r][mid] == target:
                    return True
                elif matrix[r][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        return False