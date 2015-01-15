
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
         n = len(S)
         m = len(T)
         if m > n:
           return 0
         path = [0 for j in xrange(m+1)]
         path[0] = 1
         
         for j in xrange(1, n+1):
           for i in xrange(1, m+1):
             if T[-i] == S[j-1]:
               path[-i] += path[-(i+1)]
         return path[m]
             
             
                                                 
def main():
  s = Solution()
  print s.numDistinct("rabbbit","rabbit")
  

if __name__ == "__main__":
    main()