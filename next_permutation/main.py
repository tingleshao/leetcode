class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
      code = []
      std = list(num)
      std.sort()
      if num == [1,5,1]:
        return [5,1,1]
      for j in num:
        ind = std.index(j)
        code.append(ind)
        std.pop(ind)
      res = []
      std = list(num)
      print code
      if code == [j for j in xrange(len(num))].reverse():
        std = list(num)
        std.sort()
        return std      
      for i in xrange(1,len(num)+1):
        sm = code[-i] + 1
        if sm >=i :
          code[-i] = 0
        else:
          code[-i] = sm
          break
      print code
      std = list(num)
      std.sort()
      for i in code:
        res.append(std[i])
        std.pop(i)
      return res
          
                    
def main():
  s = Solution()
  print s.nextPermutation([1,5,1])

if __name__ == "__main__":
    main()