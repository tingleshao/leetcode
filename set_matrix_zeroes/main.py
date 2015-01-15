class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
      m = len(matrix)
      n = len(matrix[0])
      for i in xrange(m):
        for j in xrange(n):
          if matrix[i][j] == 0:
            for k in xrange(n):
              if matrix[i][k] != 0:
                matrix[i][k] = None
            for l in xrange(m):
              if matrix[l][j] !=0
                matrix[l][j] = None
      for i in xrange(m):
        for j in xrange(n):
          if matrix[i][j] == None:
            matrix[i][j] = 0
          
        
    
def main():
  s = Solution()
  m = [[1,0],[0,4]]
  print s.setZeroes(m)
  print m
     
if __name__ == "__main__":
    main()
    