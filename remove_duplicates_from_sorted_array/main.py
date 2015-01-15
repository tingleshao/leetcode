class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
         if len(A) < 2:
           return len(A)
         idx = 1 
         for i in xrange(1,len(A)):
           if A[i] != A[i-1]:
             A[idx] = A[i]
             idx += 1
         return idx