# Matrix is sorted thus, Binary Search can be used!


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # if len(matrix) == 0:return False

        # start = 0
        # # rows x columns - 1 (because python_list is `0 indexed`)
        # end = len(matrix) * len(matrix[0]) -1

        # if len(matrix) == 0:
        #     return False

        # while start <= end:

        #     mid = (start + end)//2

        #     #
        #     mid_row = (mid // len(matrix[0])) # rowNo. for middle index
        #     mid_col = (mid % len(matrix[0]))  # colNo. for middle index


        #     if matrix[mid_row][mid_col] == target:
        #         return True
            
        #     elif matrix[mid_row][mid_col] < target:
        #         start = mid + 1
            
        #     else:
        #         end = mid - 1
        
        # return False
        
        
        
        """ 
        Instead of dividing the search space in half at each step, it starts at the top right corner of the matrix and compares the current element to the target. 
        If the current element is less than the target, it moves to the next row, since all elements in the current column will be less than the target. 
        If the current element is greater than the target, it moves to the previous column, since all elements in the current row will be greater than the target. 
        This continues until the target is found or the entire matrix has been searched."""

        # Matrix Empty or Not!
        if len(matrix) == 0 :
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0 :

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                # # Current element is less than target, move to next row
                row += 1

            else:
                # # Current element is greater than target, move to previous column
                col -= 1 
        return False


 