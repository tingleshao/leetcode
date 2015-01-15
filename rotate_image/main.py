class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n/2):
            for j in xrange(i,n-1-i):
                temp = matrix[n-1-j][i]
         #       print i 
        #        print j
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                
                matrix[j][n-1-i] = matrix[i][j]
                
                matrix[i][j] = temp
        return matrix

    
def main():
  s = Solution()
  matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
  matrix2 = [[1,2],[3,4]]
  matrix3 = 	[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
  print s.rotate(matrix1)
     
if __name__ == "__main__":
    main()
    