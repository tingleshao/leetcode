class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        dp = [False for i in xrange(n+1)]
        dp[n] = True
        for i in xrange(n-1,-1,-1):
          for j in xrange(i,n):
            ss = s[i:j+1]
            if ss in dict and dp[j+1]:
              dp[i] = True
              break
        return dp[0]      

def main():
    s = Solution()
    n1 = ListNode(0)
    n2 = ListNode(1)
    t = [n1,n2]
    
    s.mergeKLists(t)
  
if __name__ == "__main__":
    main()