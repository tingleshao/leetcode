class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        if len(S) == 0:
          return res
        S.sort()
        prev = []
        for x in S:
          for i in xrange(len(res)):
            ss = list(res[i])
            ss.append(x)
            if not ss in res:
              res.append(ss)
        return res
				
				
    
def main():
  s = Solution()
  S = [1,2,2]
  print s.subsetsWithDup(S)


     
if __name__ == "__main__":
    main()
                