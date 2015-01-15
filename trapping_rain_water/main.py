class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        low = 0
        high = 0
        wsum = 0
        for i in xrange(len(A)):
          print "i " + str(i)
          if low < high:
            low = i
            print "yes " + str(high) + " " + str(low)            
          if A[i] >= A[low]:
            if A[i] >= A[high]:
              high = i
              print "high " + str(high) + " " + str(low)
            else:
              low = i
            if high <= low:
              wsum += min(A[i],A[high]) - A[low]
            print "yes2 " + str(high) + " " + str(low) 
          else:
            low = i  
            wsum += A[high] - A[low]
            print "yes3 " + str(high) + " " +str(low)
            
        return wsum
            
				
          
          
    
def main():
  s = Solution()
  A = [0,1,0,2,1,0,1,3,2,1,2,1]
  B = [2,0,2]
  C = [4,2,3]
  print s.trap(C)
  
  
     
if __name__ == "__main__":
    main()