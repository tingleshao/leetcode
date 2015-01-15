class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
      ret = 0
      last = 0
      curr = 0
      for i in xrange(len(A)):
        if i> last:
          last = curr
          ret +=1
        curr = max(curr,i+A[i])
        
      return ret
                                                         
def main():
  s = Solution()
  A = [2,3,1,1,4]
  print s.jump(A)
  

if __name__ == "__main__":
    main()