class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left = 0
        right = len(A) -1
        alls = 0
        block = 0
        currLevel = 0
        while left <= right:
          if min([A[left],A[right]]) > currLevel:
            alls += (right-left+1)*(min([A[left],A[right]]) -currLevel)
            currLevel = min([A[left],A[right]]) 
          if A[left]<A[right]:
            block += A[left]
            left += 1
          else:
            block += A[right]
            right -=1
        return alls - block
        
        
            
				
          
          
    
def main():
  s = Solution()
  A = [0,1,0,2,1,0,1,3,2,1,2,1]
  B = [2,0,2]
  C = [4,2,3]
  print s.trap(A)
  
  
     
if __name__ == "__main__":
    main()