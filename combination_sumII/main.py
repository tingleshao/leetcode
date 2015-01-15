class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        ans = []
        if len(candidates) == 0:
          return ans 
        candidates.sort()
        end = len(candidates)
        ll = []
        start = 0
        pool = candidates 
        self.comb(target,start,end,ll,ans,pool)
        ans2 = []
        for item in ans:
          if not item in ans2:
            ans2.append(item)
        return ans2
        
    def comb(self,target,start,end,ll,ans,pool):
      if target < 0 or start >= pool:
        return 
      if target == 0:
     #   if not ll in ans:
        ans.append(ll)
        return 
      else: 
        for i in range(start,end):
          lst = ll[:]
          lst.append(pool[i])
          self.comb(target-pool[i],i+1,end,lst,ans,pool)
       #   if len(ll) > 0:
       #     ll.pop(-1)
      
        

def main():
  s = Solution()
  can = [10,1,2,7,6,1,5]
  can2 = [1]#
  can3 = [14,22,8,31,30,26,9,34,20,13,10,22,6,12,18,22,28,19,14,17,24,24,22,14,27,30,6,23,25,14,33,5,23,7,23,18,28,20,9,5,20,14,22,21,21,6,9,6,12,10,19,31,21,28,32,14,23,33,32,14]
  print s.combinationSum2(can,8)
  print s.combinationSum2(can2,1)
  print s.combinationSum2(can3,29)



if __name__ == "__main__":
    main()
                