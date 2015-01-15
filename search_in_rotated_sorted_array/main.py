class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
      if target in A:
        return A.index(target)
      return -1
    
def main():
  s = Solution()
  print s.search([3])
     
if __name__ == "__main__":
    main()
    