class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
          return 0
        for i in xrange(m):
          for j in xrange(n):
            if i == 0:
            #  print "foo"
              if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = -1
                if m == 1:
                  return 0
              elif j == 0 or obstacleGrid[i][j-1] > 0:
                obstacleGrid[i][j] = 1
            elif j == 0:
              if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = -1
                if n == 1:
                  return 0
              elif obstacleGrid[i-1][j] > 0:
                obstacleGrid[i][j] = 1
            elif obstacleGrid[i][j] == 1:
              obstacleGrid[i][j] = -1
  #      print obstacleGrid
        for i in xrange(1,m):
          for j in xrange(1,n):
            if obstacleGrid[i][j] != -1:
              if obstacleGrid[i-1][j] == -1:
                if obstacleGrid[i][j-1] == -1:
                  obstacleGrid[i][j] = 0
                else:
                  obstacleGrid[i][j] = obstacleGrid[i][j-1]
              elif obstacleGrid[i][j-1] == -1:
                obstacleGrid[i][j] = obstacleGrid[i-1][j]
              else:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
    #    print obstacleGrid
        
        return obstacleGrid[m-1][n-1]
        
    
def main():
  s = Solution()
  g = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
  ]
  g2 = [[1]]
  g3 = [[1],[0]]
  g4 = [[0,0],[0,1]]
  g5 = [[0,1],[1,0]]
  g6 = [[0,0],[1,1],[0,0]]
  g7 = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
  g8 = [[0]]
  print s.uniquePathsWithObstacles(g)
  print s.uniquePathsWithObstacles(g2)
  print s.uniquePathsWithObstacles(g3)
  print s.uniquePathsWithObstacles(g4)
  print s.uniquePathsWithObstacles(g5)
  print s.uniquePathsWithObstacles(g6)
  print s.uniquePathsWithObstacles(g7)
  print s.uniquePathsWithObstacles(g8)
     
if __name__ == "__main__":
    main()
                     
        
                
                
          
				
				