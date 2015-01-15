class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
      if len(A) <= 1:
        return True
      step = A[0]
      n = len(A)
      ii = 0
      for i in xrange(1,len(A)):
        if step == 0 or (i + step) >= n:
          break
        print "step: " + str(step)
        print "i: "  + str(i)
        step =  max(step-1,A[i])
        
        
      return step != 0
		
		
    
def main():
  s = Solution()
  A1 = [2,3,1,1,4]
  A2 = [3,2,1,0,4]
  A3 = [2,0,0]
  print s.canJump(A1)
  print s.canJump(A2)
  print s.canJump(A3)
  
  
  

     
if __name__ == "__main__":
    main()
                     
       