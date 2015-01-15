class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
      if A == []:
        return 0
      else:
        return self.binSearch(A,target,0,len(A)) 
        
        
    def binSearch(self,A,target,left,right):
   #   print target,left,right
      
      if left >= right:
        if left >= len(A):
          return len(A)
        if A[left] > target:
          return left
        else:
          return left +1
      mid = left + ( right - left )  / 2
      if A[mid] == target:
        return mid
      elif A[mid] > target:
        return self.binSearch(A,target,left,mid)
      else:
        return self.binSearch(A,target, mid+1,right)
      
      
def main():
    s = Solution()
    A = [1,3,5,6]
    print s.searchInsert(A,5)
    print s.searchInsert(A,2)
    print s.searchInsert(A,7)
    print s.searchInsert(A,0)
    
    
if __name__ == "__main__":
    main()
        