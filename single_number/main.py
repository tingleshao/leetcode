class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = A[0]
        for i in xrange(len(A)):
          result ^= A[i]
        return result
        
                
def main():  
    s = Solution()
    print s.preorderTraversal(n1)

if __name__ == "__main__":
    main()