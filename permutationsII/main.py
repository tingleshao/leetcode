
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if num == []:
          return []
        res = []
        code = [0 for i in xrange(len(num))]
        final = range(len(num))
        final.reverse()
#        pdict = {}
        while code != final:
           per = []
           numm = list(num)
           numm.sort()
           for j in code:
             per.append(numm[j])
             numm.pop(j)
           if not per in res:
             res.append(per)
           for j in xrange(1,len(code)+1):
             sm = code[-j] + 1
             if sm == j:
               code[-j] = 0
             else:
               code[-j] = sm
               break
        return res
                
        
                            
def main():
  s = Solution()
  print s.permuteUnique([1,1,2])

if __name__ == "__main__":
    main()