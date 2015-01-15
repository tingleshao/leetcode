class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        s = [0 for i in xrange(n+1)]
        s[0] = 1
        s[1] = 1
        for j in xrange(2,n+1):
          s[j] = s[j-1]+s[j-2] 
        return s[n]