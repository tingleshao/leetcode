class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
      strsort = []
      strDict = {}
      res = []
      for i in xrange(len(strs)):
        s = strs[i]
        ss = ".".join(sorted(s))
        if strDict.has_key(ss):
          strDict[ss][1] +=1
          strDict[ss][0].append(i)
        else:
          strDict[ss] = [[i],1]
      for k in strDict.keys():
        if strDict[k][1] > 1:
          for s in strDict[k][0]:
            res.append(strs[s])
      return res
        
			

def main():
  s = Solution()
  xx = ["abc","bca","aaa"]
  print s.anagrams(xx)



if __name__ == "__main__":
    main()
             