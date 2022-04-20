#Example 1:

#Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#Output: 8
#Explanation: There are 8 negatives number in the matrix.
#Example 2:

#Input: grid = [[3,2],[1,0]]
#Output: 0

def countNegatives(grid):
    row = len(grid)-1      # row and column
    col = len(grid[0])-1
    
    if grid[row][col] > 0:
        return 0
    
    if grid[0][0] < 0:
        return (row + 1) * (col+ 1) 
    
    i = 0
    j = col
    negativeCount = 0
    while i <= row and j >= 0:
        if grid[i][j] < 0:
            negativeCount += row + 1 - i
            j -= 1
        else:
            i += 1
    print(negativeCount)
    return negativeCount