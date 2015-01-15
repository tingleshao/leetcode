class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        for j in xrange(len(B)):
          A[m+j] = B[j]
        A.sort()
        
                				
def main():  
    A = [0]
    B = [1]
    s = Solution()
    s.merge(A,0,B,1)
    print A

if __name__ == "__main__":
    main()