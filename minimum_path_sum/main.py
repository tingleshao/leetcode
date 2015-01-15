class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
      m = len(grid)
      n = len(grid[0])
      sumGrid = []
      for i in xrange(m):
        sumGrid.append([])
        for j in xrange(n):
          if i == 0:
            sumGrid[i].append(grid[0][j])
          elif j == 0:
            sumGrid[i].append(grid[i][0])
          else:
            sumGrid[i].append(0)
      for i in xrange(1,m):
        sumGrid[i][0] = sumGrid[i-1][0]+sumGrid[i][0]
      for j in xrange(1,n):
        sumGrid[0][j] = sumGrid[0][j-1]+sumGrid[0][j]
      for i in xrange(1,m):
        for j in xrange(1,n):
          sumGrid[i][j] = min([sumGrid[i-1][j],sumGrid[i][j-1]]) + grid[i][j]
      return sumGrid[-1][-1]
        
    
def main():
  s = Solution()
  grid = [[1,2,1],[3,1,1]]
  print s.minPathSum(grid)
     
if __name__ == "__main__":
    main()
    