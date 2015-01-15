class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
          return 0
          
        maxherepre = A[0]
        minherepre = A[0]
        maxsofar = A[0]
        maxhere = 0
        minhere = 0
        
        for i in xrange(1,len(A)):
          maxhere = max(max(maxherepre * A[i], minherepre * A[i]), A[i])
          minhere = min(min(maxherepre * A[i], minherepre * A[i]), A[i])
          if maxhere > maxsofar:
            maxsofar = maxhere
          maxherepre = maxhere
          minherepre = minhere
        
        return maxsofar                     
def main():
    s = Solution()
    i1 = Interval(5,7)
    i2 = Interval(1,5)
    i3 = Interval(2,3)
    
    print s.insert([],i1)
    xx = s.insert([i2],i3)
    print xx[0].start, xx[0].end
    
    
if __name__ == "__main__":
    main()