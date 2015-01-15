class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
          return
        itor = 2
        lens = 2
        n = len(A)
        while itor < n:
          if A[itor] != A[lens-2]:
            A[lens] = A[itor]
            lens += 1
          itor += 1
        del A[lens:]  
        return lens
        
    
  
def main():
  s = Solution()
  A = [1,1,1,2,2,3]
  print s.removeDuplicates(A)
  print A
     
if __name__ == "__main__":
    main()
    