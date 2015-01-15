class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        m = []
        for i in xrange(n):
          m.append([])
          for j in xrange(n):
            m[i].append(0)
        count = 1
        for i in xrange((n+1)/2):
          for j in xrange(i,n-1-i):
            m[i][j] = count
            count +=1
          for j in xrange(i,n-1-i):
            m[j][n-1-i] = count
            count += 1
          for j in xrange(i,n-1-i):
            m[n-1-i][n-1-j] = count
            count += 1
          for j in xrange(i,n-1-i):
            m[n-1-j][i] = count
            count += 1
            
        if n % 2 == 1:
          m[n/2][n/2] = count
        return m
				
def main():
  s = Solution()
 
  print s.generateMatrix(5)
     
if __name__ == "__main__":
    main()
    