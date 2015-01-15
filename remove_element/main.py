class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        j = len(A)-1
        i = 0
        if len(A) == 0:
          return []
        while i <= j:
          if A[i] == elem:
            while i <= j:
              if A[j] != elem:
                A[i] = A[j]
                j-=1
                break
              j-=1
          i+=1
        return j+1
        
                              
def main():
    s = Solution()
    print s.removeElement([],0) 
    print s.removeElement([1],1) 
    
    
if __name__ == "__main__":
    main()