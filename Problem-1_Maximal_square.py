# APPROACH  1: BRUTE FORCE
# Time Complexity : O((m * n) ^ 2), m: # of rows of matrix, n: # of columns in matrix
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Go thru each element of the matrix and check further only if the cell value is 1.
# 2. Then, go to it's next diaginal element and check if all elements in that row and column are 1's. (bounded by the initial element).
# 3. If not, stop checking and move to next cell and also update the max length found so far. If so, go to next diagonal element and keep track of the length of diagonal found 
#    so far. 
# 4. Return area as (max length * max length), as length of diagonal same as the length of side of square. 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if matrix is None or len(matrix) == 0:
            return 0
        
        row, col, max_len = len(matrix), len(matrix[0]), 0
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    curr_len, isZero = 1, False
                    
                    while not isZero and i + curr_len < row and j + curr_len < col:
                        for k in range(i + curr_len, i - 1, -1):
                            if matrix[k][j + curr_len] == '0':
                                isZero = True
                                break
                                
                        if isZero:
                            break
                            
                        for k in range(j + curr_len, j - 1, -1):
                            if matrix[i + curr_len][k] == '0':
                                isZero = True
                                break
                        
                        if not isZero:
                            curr_len += 1
                        
                    max_len = max(max_len, curr_len)
                    
        return max_len * max_len
        
        
        
        

# APPROACH  2: OPTIMAL APPROACH
# Time Complexity : O(m * n), m: # of rows of matrix, n: # of columns in matrix
# Space Complexity : O(m * n), size of dp
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Create a dp matrix with one extra row and one extra column of 0s. 
# 2. Start filling it from second row and second column onwards. Fill only if the cell in the original matrix is 1 else leave it as 0.
# 3. to fill a cell, take minimum of it's left neightbor, top neighbor and top-left neighbor. Add one to it. (Do this as the length of the square at this point is constrained 
#    by the min val of it's neighbors. Think of this cell as the bottom-rightmost corner of the current square being considered.)
# 4. While filling, keep track of the max length found so far and at end return the area corresponding to it. 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if matrix is None or len(matrix) == 0:
            return 0
        
        row, col, max_len = len(matrix), len(matrix[0]), 0
        
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    max_len = max(max_len, dp[i][j])
            
        return max_len * max_len
                
