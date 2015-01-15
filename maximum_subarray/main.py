class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
      if A == []:
        return 0
      maxsofar = A[0]
      currmax = A[0]
      for i in xrange(1,len(A)):
        currmax = max(A[i],currmax+A[i])
        if currmax > maxsofar:
          maxsofar = currmax
      return maxsofar 
        
def main():
    s = Solution()
    
    print s.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])
  
if __name__ == "__main__":
    main()