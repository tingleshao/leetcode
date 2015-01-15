class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
      m = len(matrix)
      if matrix == []:
        return []
      n = len(matrix[0])
      s = min(m,n)
      lst = []
      if m == 1:
          return matrix[0]
      if n == 1:
          for i in xrange(m):
              lst.append(matrix[i][0])
          return lst
      for i in xrange((s+1)/2):
        for j in xrange(i,n-1-i):
          lst.append(matrix[i][j])
        for j in xrange(i,m-1-i):
          lst.append(matrix[j][n-1-i])
        for j in xrange(i,n-1-i):
          lst.append(matrix[m-1-i][n-1-j])
        for j in xrange(i,m-1-i):
          lst.append(matrix[m-1-j][i])
      if n % 2 ==1 and m % 2 == 1:
        lst.append(matrix[m/2][n/2])
      return lst
    
def main():
  s = Solution()
  m = [
  [ 1, 2 ],
  [ 4, 5],
  [ 7, 8]
  ]
  print s.spiralOrder(m)
     
if __name__ == "__main__":
    main()
    