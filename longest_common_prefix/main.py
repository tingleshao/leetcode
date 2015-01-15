class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
      if len(strs) == 0:
        return ""
      if len(strs[0]) == 0:
        return ""
      lcp = len(strs[0]) - 1
      for j in xrange(1,len(strs)):
      
        for i in xrange(len(strs[0])): # change this upper bound to lcp may speed up the process
          if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
            lcp = min(lcp,i-1)
      print lcp
      return strs[0][:lcp+1]
        
				
				
def main():
  s = Solution()
  g8 = ["abc","ab","abcd"]
  g1 = ["abab","aba",""]
  print s.longestCommonPrefix(g8)
  print s.longestCommonPrefix(g1)
  

     
if __name__ == "__main__":
    main()
                   
                   