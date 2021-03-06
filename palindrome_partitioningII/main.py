class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
      n = len(s)
      cut = [i-1 for i in xrange(n+1)]
      for i in xrange(n):
        j = 0
        while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
          cut[i+j+1] = min(cut[i+j+1],1+cut[i-j])
          j+=1
        j = 1
        while i-j+1 >= 0 and i+j < n and s[i-j+1] == s[i+j]:
          cut[i+j+1] = min(cut[i+j+1],1+cut[i-j+1])
          j+=1
      return cut[n]
        
      
def main():  
    s = Solution()
    strs = "aab"
    print s.minCut(strs)

if __name__ == "__main__":
    main()