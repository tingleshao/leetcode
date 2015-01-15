class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
      if len(num) == 1:
        return [num]
      else:
        pers = []
        for i in xrange(len(num)):
          subNum = num[:i] + num[i+1:]
          subPers = self.permute(subNum)
          for p in subPers:
            pers.append([num[i]]+p)
        return pers
        
				
def main():
  s = Solution()
  print s.permute([1,2,3])
     
if __name__ == "__main__":
    main()
    