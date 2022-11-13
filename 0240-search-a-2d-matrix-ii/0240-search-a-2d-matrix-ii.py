class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         #binary search in each column
#         #linear in each row
        
#         for r in range(len(matrix)):
#             low = 0
#             high = len(matrix[r]) - 1
            
#             while (low <= high):
#                 mid = (low + high) // 2
#                 if matrix[r][mid] == target:
#                     return True
#                 elif matrix[r][mid] > target:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#         return False
#     #runtime O(mlogn)
    
    #runtime O(n+m)
     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            # compare target with matrix[row][col]?????
            # search space reduce
            m = len(matrix)
            n = len(matrix[0])
            
            row = 0
            col = n - 1
            while (row < m and col >= 0):
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            
            return False