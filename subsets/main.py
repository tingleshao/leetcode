class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        A = [[]]
        S.sort()
        for n in S:
          for j in xrange(len(A)):
            ss = list(A[j])
            ss.append(n)
            A.append(ss)
        return A
        
    
def main():
  s = Solution()
  print s.subsets([1,2,3])

     
if __name__ == "__main__":
    main()