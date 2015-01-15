class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
      return self.tabulate(m,n)
      
    def route(self,j,k):
      if j == 1 or k == 0:
        return 1
      if k == 1:
        return j
      sum = 0
      for i in range(1,j+1):
        sum = sum + self.route(j+1-i,k-1)
      return sum
      
    def tabulate(self,m,n):
      table = []
      for i in xrange(m):
        table.append([])
        for j in xrange(n):
          table[i].append(0)
          
      for j in xrange(1,n):
        table[0][j] = 1
      for i in xrange(m):
        table[i][0] = 1
        
      for i in xrange(1,m):
        for j in xrange(1,n):
          table[i][j] = table[i-1][j] + table[i][j-1]
          
      return table[m-1][n-1]    
    
        
    
def main():
  s = Solution()
  print s.uniquePaths(3,3)
     
if __name__ == "__main__":
    main()
    